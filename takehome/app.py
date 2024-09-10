from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from takehome import logger
from takehome.config import settings

# ============================ Team Matcher Server ============================

# Note to challengers:
# You may add additional files as needed to complete the challenge.

# Docs:
# - FastAPI: https://fastapi.tiangolo.com/

# You may modify this file as needed.

# =============================================================================

MOCK_FLAKY_ENDPOINT = "http://localhost:8001/generate_score"
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=Path(BASE_DIR, "templates"))


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    logger.info("Secret Key: %s", settings.SECRET_KEY)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )
