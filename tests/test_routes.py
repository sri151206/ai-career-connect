"""
test_routes.py — Integration tests for route endpoints.
"""


def test_index_page(client):
    """Landing page should return 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI Career Connect' in response.data


def test_login_page(client):
    """Login page should be accessible."""
    response = client.get('/auth/login')
    assert response.status_code == 200


def test_register_page(client):
    """Register page should be accessible."""
    response = client.get('/auth/register')
    assert response.status_code == 200


def test_dashboard_requires_login(client):
    """Dashboard should redirect unauthenticated users."""
    response = client.get('/dashboard/', follow_redirects=False)
    assert response.status_code == 302
