"""
ChatHistory model — logs every conversation turn with the AI.
"""

from datetime import datetime, timezone
from app import db


class ChatHistory(db.Model):
    """Stores user ↔ AI conversation messages for context & audit."""

    __tablename__ = 'chat_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(20), nullable=False)    # 'user' or 'assistant'
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<ChatHistory {self.id} [{self.role}]>'
