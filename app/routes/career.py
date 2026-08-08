"""
career.py — Career analysis endpoints powered by Mistral AI.
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.career_profile import CareerProfile
from app.models.chat_history import ChatHistory
from app.services.mistral_service import get_career_recommendation, chat_with_ai

career_bp = Blueprint('career', __name__)


@career_bp.route('/analyze', methods=['GET', 'POST'])
@login_required
def analyze():
    """Accept user skills/interests, call Mistral, and store the result."""
    if request.method == 'POST':
        skills = request.form.get('skills', '')
        interests = request.form.get('interests', '')
        experience = request.form.get('experience_level', 'entry')

        recommendation = get_career_recommendation(skills, interests, experience)

        profile = CareerProfile(
            user_id=current_user.id,
            skills=skills,
            interests=interests,
            experience_level=experience,
            ai_recommendation=recommendation,
        )
        db.session.add(profile)
        db.session.commit()

        return render_template('career/result.html', profile=profile)

    return render_template('career/analyze.html')


@career_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    """Multi-turn AI chat — sends conversation context to Mistral."""
    user_message = request.json.get('message', '')

    # Persist user message
    db.session.add(ChatHistory(
        user_id=current_user.id, role='user', message=user_message
    ))
    db.session.commit()

    # Build conversation context from recent history
    history = ChatHistory.query.filter_by(user_id=current_user.id) \
                               .order_by(ChatHistory.created_at.desc()) \
                               .limit(20).all()
    history.reverse()

    messages = [{'role': h.role, 'content': h.message} for h in history]
    ai_response = chat_with_ai(messages)

    # Persist assistant reply
    db.session.add(ChatHistory(
        user_id=current_user.id, role='assistant', message=ai_response
    ))
    db.session.commit()

    return jsonify({'response': ai_response})
