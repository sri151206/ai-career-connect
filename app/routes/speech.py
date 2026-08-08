"""
speech.py — Speech-to-Text and Text-to-Speech endpoints.
"""

import os
from flask import Blueprint, request, jsonify, send_file, current_app
from flask_login import login_required

from app.services.speech_service import transcribe_audio, synthesize_speech

speech_bp = Blueprint('speech', __name__)


@speech_bp.route('/to-text', methods=['POST'])
@login_required
def speech_to_text():
    """Accept an audio file upload and return the transcribed text."""
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    upload_dir = current_app.config['SPEECH_UPLOAD_FOLDER']
    os.makedirs(upload_dir, exist_ok=True)

    filepath = os.path.join(upload_dir, audio_file.filename)
    audio_file.save(filepath)

    try:
        text = transcribe_audio(filepath)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Clean up the temporary file
        if os.path.exists(filepath):
            os.remove(filepath)


@speech_bp.route('/to-speech', methods=['POST'])
@login_required
def text_to_speech():
    """Accept text and return a synthesized audio file."""
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        audio_path = synthesize_speech(text)
        return send_file(audio_path, mimetype='audio/mp3', as_attachment=True,
                         download_name='response.mp3')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
