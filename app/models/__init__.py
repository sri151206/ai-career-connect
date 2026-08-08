"""
app/models/__init__.py - Database Models Package
=================================================
WHY THIS FOLDER EXISTS:
  Each file in models/ defines one SQLAlchemy ORM model (one database table).
  Splitting models into separate files keeps them maintainable as the schema
  grows. This __init__.py re-exports them so the rest of the app can do:
      from app.models import User, CareerProfile, ChatHistory
"""

from app.models.user import User
from app.models.career_profile import CareerProfile
from app.models.chat_history import ChatHistory

__all__ = ['User', 'CareerProfile', 'ChatHistory']
