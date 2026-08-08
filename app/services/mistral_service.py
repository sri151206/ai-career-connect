"""
mistral_service.py — All interactions with the Mistral AI API.
===============================================================
WHY THIS FILE EXISTS:
  Isolates every Mistral API call behind clean Python functions.
  If the API version changes or we switch to a different LLM provider,
  only this file needs updating — zero route changes required.

NOTE:
  Uses raw HTTP via `requests` instead of the `mistralai` SDK to avoid
  Windows Long Path issues with the SDK's deeply nested file structure.
"""

import os
import requests

MISTRAL_API_URL = 'https://api.mistral.ai/v1/chat/completions'


def _get_headers():
    """Build authorisation headers for the Mistral API."""
    api_key = os.environ.get('MISTRAL_API_KEY', '')
    if not api_key:
        raise RuntimeError(
            'MISTRAL_API_KEY is not set. '
            'Add it to your .env file or export it as an environment variable.'
        )
    return {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }


def _call_mistral(messages: list[dict], model: str | None = None) -> str:
    """
    Send a chat-completion request to the Mistral REST API.

    Args:
        messages: List of message dicts with 'role' and 'content'.
        model:    Model name override (defaults to env MISTRAL_MODEL).

    Returns:
        The assistant's reply text.

    Raises:
        RuntimeError: If the API key is missing or the request fails.
    """
    model = model or os.environ.get('MISTRAL_MODEL', 'mistral-large-latest')

    payload = {
        'model': model,
        'messages': messages,
    }

    try:
        response = requests.post(
            MISTRAL_API_URL,
            headers=_get_headers(),
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as e:
        error_detail = ''
        try:
            error_detail = e.response.json().get('message', str(e))
        except Exception:
            error_detail = str(e)
        raise RuntimeError(f'Mistral API error: {error_detail}')
    except requests.exceptions.ConnectionError:
        raise RuntimeError('Could not connect to the Mistral API. Check your internet connection.')
    except requests.exceptions.Timeout:
        raise RuntimeError('Mistral API request timed out. Please try again.')
    except (KeyError, IndexError):
        raise RuntimeError('Unexpected response format from the Mistral API.')


def get_career_recommendation(skills: str, interests: str, experience: str) -> str:
    """
    Build a career-counsellor prompt and return the AI's recommendation.

    Args:
        skills:      Comma-separated list of user skills.
        interests:   Free-text description of interests.
        experience:  One of 'entry', 'mid', 'senior'.

    Returns:
        The AI-generated career recommendation as a string.
    """
    system_prompt = (
        "You are an expert AI career counsellor. Based on the user's skills, "
        "interests, and experience level, provide a detailed, actionable career "
        "recommendation. Include: suggested job titles, learning roadmap, "
        "industry trends, and salary expectations."
    )

    user_prompt = (
        f"Skills: {skills}\n"
        f"Interests: {interests}\n"
        f"Experience Level: {experience}\n\n"
        "Please provide a comprehensive career recommendation."
    )

    return _call_mistral([
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ])


def chat_with_ai(messages: list[dict]) -> str:
    """
    Continue a multi-turn conversation.

    Args:
        messages: List of dicts with 'role' and 'content' keys,
                  representing the conversation so far.

    Returns:
        The assistant's latest reply.
    """
    system_message = {
        'role': 'system',
        'content': (
            "You are an AI career adviser on the AI Career Connect platform. "
            "Help users explore career paths, improve their skills, and "
            "prepare for job applications. Be encouraging and specific."
        ),
    }

    return _call_mistral([system_message] + messages)
