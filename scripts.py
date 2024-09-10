import uvicorn


def dev():
    """Start the dev server with `poetry run start` at root level"""
    uvicorn.run("takehome.app:app", host="0.0.0.0", port=8000, reload=True, reload_excludes=["takehome/mock.py"])


def mock():
    """Start the mock server with `poetry run start` at root level."""
    uvicorn.run("takehome.mock:app", host="0.0.0.0", port=8001, reload=True, reload_includes=["takehome/mock.py"], reload_excludes=["*.py"])
