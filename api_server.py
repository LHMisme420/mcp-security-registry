#!/usr/bin/env python3
import sqlite3
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json
import uuid
from datetime import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'dev-secret-change-in-prod'
jwt = JWTManager(app)

DB_FILE = 'vata.db'

def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect(DB_FILE)
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS organizations (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        api_key TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        active BOOLEAN DEFAULT 1
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS findings (
        id INTEGER PRIMARY KEY,
        org_id INTEGER NOT NULL,
        server_url TEXT NOT NULL,
        vector_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        cvss_score REAL,
        remediation TEXT,
        detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(org_id) REFERENCES organizations(id)
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS compliance_reports (
        id INTEGER PRIMARY KEY,
        org_id INTEGER NOT NULL,
        framework TEXT NOT NULL,
        compliance_score REAL,
        report_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(org_id) REFERENCES organizations(id)
    )''')
    
    conn.commit()
    conn.close()

init_db()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'version': '1.0.0'}), 200

@app.route('/auth/register', methods=['POST'])
def register():
    """Register new organization"""
    data = request.json
    org_name = data.get('org_name')
    
    if not org_name:
        return jsonify({'error': 'org_name required'}), 400
    
    api_key = str(uuid.uuid4())
    
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO organizations (name, api_key) VALUES (?, ?)",
            (org_name, api_key)
        )
        conn.commit()
        org_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'org_id': org_id,
            'api_key': api_key,
            'message': 'Organization created'
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/auth/login', methods=['POST'])
def login():
    """Get JWT token using API key"""
    api_key = request.json.get('api_key')
    
    if not api_key:
        return jsonify({'error': 'api_key required'}), 400
    
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM organizations WHERE api_key = ? AND active = 1", (api_key,))
        org = cursor.fetchone()
        conn.close()
        
        if not org:
            return jsonify({'error': 'Invalid API key'}), 401
        
        access_token = create_access_token(identity=str(org["id"]))
        return jsonify({'access_token': access_token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/findings', methods=['GET'])
@jwt_required()
def list_findings():
    """List all findings for org"""
    org_id = int(get_jwt_identity())
    
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM findings WHERE org_id = ? ORDER BY detected_at DESC LIMIT 100",
            (org_id,)
        )
        findings = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return jsonify({'findings': findings}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/reports/compliance', methods=['POST'])
@jwt_required()
def generate_compliance_report():
    """Generate compliance report"""
    org_id = int(get_jwt_identity())
    data = request.json
    framework = data.get('framework', 'SOC2')
    
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT severity, COUNT(*) as count FROM findings WHERE org_id = ? GROUP BY severity",
            (org_id,)
        )
        severity_counts = {row[0]: row[1] for row in cursor.fetchall()}
        
        total_vulns = sum(severity_counts.values())
        compliance_score = max(0, 100 - (total_vulns * 5))
        
        report_json = {
            'framework': framework,
            'severity_breakdown': severity_counts,
            'compliance_score': compliance_score,
            'generated_at': datetime.now().isoformat()
        }
        
        cursor.execute(
            "INSERT INTO compliance_reports (org_id, framework, compliance_score, report_json) VALUES (?, ?, ?, ?)",
            (org_id, framework, compliance_score, json.dumps(report_json))
        )
        conn.commit()
        report_id = cursor.lastrowid
        conn.close()
        
        return jsonify({
            'report_id': report_id,
            'compliance_score': compliance_score,
            'framework': framework,
            'severity_breakdown': severity_counts
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
