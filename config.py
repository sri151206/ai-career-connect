"""
config.py - Application Configuration
======================================
Centralizes ALL configuration settings (DB paths, API keys, secret keys, etc.)
so that nothing is hardcoded across the codebase. Supports multiple environments
(development, testing, production) via class inheritance.
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration shared across all environments."""

    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

    # ── Database ─────────────────────────────────────────────────────
    raw_db_url = os.environ.get('DATABASE_URL')
    if raw_db_url and raw_db_url.startswith("postgres://"):
        raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = raw_db_url or f'sqlite:///{os.path.join(BASE_DIR, "instance", "ai_career_connect.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ── Mistral AI API ───────────────────────────────────────────────
    MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY', '')
    MISTRAL_MODEL = os.environ.get('MISTRAL_MODEL', 'mistral-large-latest')

    # ── File Upload Settings ─────────────────────────────────────────
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload

    # ── Speech Settings ──────────────────────────────────────────────
    SPEECH_UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'audio')
    ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'webm', 'flac'}


class DevelopmentConfig(Config):
    """Development-specific settings."""
    DEBUG = True


class TestingConfig(Config):
    """Testing-specific settings - uses an in-memory DB."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Production-specific settings."""
    DEBUG = False
    # In production, SECRET_KEY *must* come from the environment
    SECRET_KEY = os.environ.get('SECRET_KEY')


config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
