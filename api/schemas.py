from pydantic import BaseModel
from typing import List
from typing import Literal

# Schema for receiving data from the frontend
class QuizResponse(BaseModel):
    name: str
    email: str
    field: str
    level: str
    gender: Literal[0, 1]
    extracurricular: str
    volunteering: Literal[0, 1]
    ethnicity: Literal[0, 1]

# Schema for the response sent back to the frontend
class ClubRecommendationResponse(BaseModel):
    recommendations: List[str]