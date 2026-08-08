"""
app/__init__.py - Application Factory
=======================================
WHY THIS FILE EXISTS:
  Flask best practice is the "Application Factory" pattern. Instead of
  creating a global `app` object, we have a `create_app()` function that
  builds and configures the app. This lets us:
    • Create multiple app instances (useful for testing)
    • Defer extension initialisation until config is loaded
    • Keep the import graph clean (no circular imports)
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import config_by_name

# ── Extensions (initialised without an app — bound later) ───────
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name='default'):
    """Build and return a fully configured Flask application."""

    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static',
    )

    # Load configuration
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Bind extensions to this app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # ── Register Blueprints ──────────────────────────────────────
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.career import career_bp
    from app.routes.speech import speech_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(career_bp, url_prefix='/career')
    app.register_blueprint(speech_bp, url_prefix='/speech')

    # Create database tables on first request
    with app.app_context():
        from app import models  # noqa: F401  — ensures models are registered
        db.create_all()

    return app
