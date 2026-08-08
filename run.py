"""
run.py - Application Entry Point
=================================
The single command to start the server:  python run.py
It imports the application factory, creates the app, and runs it.
"""

import sys
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Add mistralai package path if installed to short-path location (Windows long-path workaround)
_ml_pkgs = os.path.join(os.path.dirname(__file__), '..', 'ml_pkgs')
if os.path.isdir('c:\\ml_pkgs'):
    sys.path.insert(0, 'c:\\ml_pkgs')
elif os.path.isdir(_ml_pkgs):
    sys.path.insert(0, _ml_pkgs)

from app import create_app

env = os.environ.get('FLASK_ENV', 'production')
app = create_app(env)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=(env == 'development'), host='0.0.0.0', port=port)
