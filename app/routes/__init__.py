"""
app/routes/__init__.py - Routes / Blueprints Package
=====================================================
WHY THIS FOLDER EXISTS:
  Each file in routes/ is a Flask Blueprint — a self-contained group of
  related endpoints. Blueprints let us:
    • Split a large app into logical modules (auth, dashboard, career, speech)
    • Avoid one monolithic routes file with hundreds of endpoints
    • Mount each module at its own URL prefix (e.g. /auth, /dashboard)
"""
