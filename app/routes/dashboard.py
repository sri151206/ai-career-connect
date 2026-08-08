"""
dashboard.py — Dynamic dashboard showing career analytics & history.
"""

from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

from app.models.career_profile import CareerProfile
from app.models.chat_history import ChatHistory

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
@login_required
def index():
    """Render the main dashboard page."""
    profiles = CareerProfile.query.filter_by(user_id=current_user.id) \
                                  .order_by(CareerProfile.created_at.desc()) \
                                  .limit(10).all()
    return render_template('dashboard/index.html', profiles=profiles)


@dashboard_bp.route('/api/stats')
@login_required
def stats():
    """JSON endpoint consumed by the dashboard's JavaScript charts."""
    total_profiles = CareerProfile.query.filter_by(user_id=current_user.id).count()
    total_chats = ChatHistory.query.filter_by(user_id=current_user.id).count()

    # Aggregate skills across all profiles for the word-cloud / bar chart
    profiles = CareerProfile.query.filter_by(user_id=current_user.id).all()
    skill_counts = {}
    for p in profiles:
        if p.skills:
            for skill in p.skills.split(','):
                skill = skill.strip().lower()
                skill_counts[skill] = skill_counts.get(skill, 0) + 1

    return jsonify({
        'total_profiles': total_profiles,
        'total_chats': total_chats,
        'skill_counts': skill_counts,
    })
