"""
app/services/__init__.py - Business Logic / Services Package
=============================================================
WHY THIS FOLDER EXISTS:
  Services encapsulate all non-trivial business logic and external API calls.
  Keeping this logic OUT of routes/ means:
    • Routes stay thin (receive request → call service → return response)
    • Services are independently testable (no Flask request context needed)
    • Swapping providers (e.g. Mistral → OpenAI) requires changing ONE file
"""
