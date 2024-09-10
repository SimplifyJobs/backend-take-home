import pytest
from httpx import AsyncClient, ASGITransport

from takehome.app import app

# ============================ Candidate Server ============================

# Note to challengers:
# You may add additional files as needed to complete the challenge.

# Docs:
# - FastAPI: https://fastapi.tiangolo.com/
# - Pytest: https://docs.pytest.org/en/stable/
# - HTTPX: https://www.python-httpx.org/

# You may modify this file as needed. It is encouraged for you to reorganize the tests and use fixtures as needed.

# ===========================================================================


@pytest.mark.asyncio
async def test_index():
    """Tests that the index is an HTML response."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
