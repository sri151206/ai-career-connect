"""
test_models.py — Unit tests for database models.
"""

from app.models.user import User


def test_user_password_hashing(db):
    """Verify password is hashed and can be verified."""
    user = User(username='testuser', email='test@example.com')
    user.set_password('securepass123')

    assert user.password_hash != 'securepass123'
    assert user.check_password('securepass123') is True
    assert user.check_password('wrongpass') is False


def test_user_repr(db):
    """Verify the string representation."""
    user = User(username='alice', email='alice@example.com')
    assert repr(user) == '<User alice>'
