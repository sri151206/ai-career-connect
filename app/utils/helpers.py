"""
helpers.py — Generic utility functions used across the application.
"""

import os
from flask import current_app


def allowed_audio_file(filename: str) -> bool:
    """Check if the uploaded file has an allowed audio extension."""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in current_app.config.get('ALLOWED_AUDIO_EXTENSIONS', set())


def ensure_upload_dirs():
    """Create upload directories if they don't exist."""
    dirs = [
        current_app.config.get('UPLOAD_FOLDER', 'uploads'),
        current_app.config.get('SPEECH_UPLOAD_FOLDER', 'uploads/audio'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
