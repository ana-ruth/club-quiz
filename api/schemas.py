from pydantic import BaseModel
from typing import List

# Schema for receiving data from the frontend
class QuizResponse(BaseModel):
    name: str
    email: str
    answers: List[str]

# Schema for the response sent back to the frontend
class ClubRecommendationResponse(BaseModel):
    message: str
    recommendations: List[str]