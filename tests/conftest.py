"""
conftest.py — Shared pytest fixtures for the entire test suite.
"""

import pytest
from app import create_app, db as _db


@pytest.fixture(scope='session')
def app():
    """Create a Flask app configured for testing."""
    app = create_app('testing')
    yield app


@pytest.fixture(scope='function')
def db(app):
    """Provide a clean database for each test function."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.session.rollback()
        _db.drop_all()


@pytest.fixture(scope='function')
def client(app):
    """Provide a Flask test client."""
    return app.test_client()
