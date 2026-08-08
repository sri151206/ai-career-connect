"""
CareerProfile model — stores AI-generated career analysis results.
"""

from datetime import datetime, timezone
from app import db


class CareerProfile(db.Model):
    """Persists each career analysis a user requests from the AI."""

    __tablename__ = 'career_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skills = db.Column(db.Text, nullable=True)           # comma-separated or JSON
    interests = db.Column(db.Text, nullable=True)
    experience_level = db.Column(db.String(50), nullable=True)
    ai_recommendation = db.Column(db.Text, nullable=True)  # Mistral response
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<CareerProfile {self.id} for User {self.user_id}>'
