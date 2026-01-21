"""
Flask Backend Server - Standalone Script
Run this to start the Flask API backend server
Usage: python run_backend.py
"""

from backend_api import app

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
