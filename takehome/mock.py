# ============================= External API Mock =============================

# Note to challengers:
# This mock API simulates the behavior of a flaky endpoint.

# Key behaviors:
# - It randomly fails with a 10% chance.
# - It introduces a random latency between 0 and 100ms before responding.

# You should not modify this file.

# =============================================================================

from typing import List, NamedTuple

from pydantic import BaseModel, Field
from fastapi import FastAPI
import secrets
import time

app = FastAPI(description="Flaky Candidate Scorer API", version="0.1.0")


class SkillRating(NamedTuple):
    skill: str
    score: float

# Model for the input data, which consists of book ratings
class CandidateScoreRequest(BaseModel):
    candidate_id: str
    skills: list[SkillRating]  # Assuming ratings are float values (e.g., 4.5, 3.0, etc.)


# Response model that returns the generated book special score and related metadata
class CandidateSpecialScoreResponse(BaseModel):
    latency_ms: int
    success: bool = True
    error_log: str | None = None
    special_scores: List[float] = Field(default_factory=list)


@app.post("/generate_score", response_model=CandidateSpecialScoreResponse)
async def generate_special_candidate_score(request: CandidateScoreRequest):
    latency_ms = secrets.randbelow(100)
    # Simulate the latency
    time.sleep(0.01 * latency_ms)

    # Randomly fail with a 10% chance
    if percentage_bool(10):
        return CandidateSpecialScoreResponse(
            latency_ms=latency_ms,
            success=False,
            error_log=secrets.choice(
                [
                    "There was a network error while calling the model",
                    f"Candidate {request.candidate_id} id could not be processed",
                    f"Book {request.candidate_id} does not exist",
                    f"A server error occurred while processing the request",
                    f"Book" f"{request.candidate_id} skills are not available yet",
                ]
            ),
        )

    # Simulate the book special score generation based on the input ratings
    special_scores = [score[1] * 1.25 for score in request.skills]

    return CandidateSpecialScoreResponse(
        latency_ms=latency_ms,
        special_scores=special_scores,
    )


# Helper function to simulate a percentage chance (p must be between 0 and 100)
def percentage_bool(p: int) -> bool:
    return p > secrets.randbelow(100)
