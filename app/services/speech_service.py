"""
speech_service.py — Speech-to-Text (STT) and Text-to-Speech (TTS) logic.
=========================================================================
WHY THIS FILE EXISTS:
  Wraps the speech libraries (SpeechRecognition for STT, gTTS for TTS)
  behind simple function calls. Routes never import speech libraries
  directly — they call these functions instead. This makes it trivial
  to swap engines (e.g. Google STT → Whisper) later.
"""

import os
import tempfile

import speech_recognition as sr
from gtts import gTTS


def transcribe_audio(filepath: str) -> str:
    """
    Convert an audio file to text using Google's free speech recognition.

    Args:
        filepath: Absolute path to a WAV / FLAC / AIFF audio file.

    Returns:
        The transcribed text.

    Raises:
        ValueError: If speech could not be understood.
        RuntimeError: If the recognition service is unreachable.
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(filepath) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        raise ValueError('Could not understand the audio. Please try again.')
    except sr.RequestError as e:
        raise RuntimeError(f'Speech recognition service error: {e}')


def synthesize_speech(text: str, lang: str = 'en') -> str:
    """
    Convert text to an MP3 audio file using Google Text-to-Speech.

    Args:
        text: The text to speak.
        lang: BCP-47 language code (default: English).

    Returns:
        Absolute path to the generated MP3 file.
    """
    tts = gTTS(text=text, lang=lang)

    # Write to a temp file that the caller can serve or stream
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(tmp.name)
    tmp.close()

    return tmp.name
