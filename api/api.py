from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .schemas import QuizResponse, ClubRecommendationResponse
from fastapi import APIRouter
import mysql.connector
from .datab import Database

router = APIRouter()

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # React default port
    "http://127.0.0.1:5500",  # Your frontend origin
    "http://localhost:5500",  # Alternative frontend origin
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
)

db = Database.connect_to_database()

@app.post("/quiz", response_model=ClubRecommendationResponse)
async def process_quiz(quiz_data: QuizResponse):
    db = Database.connect_to_database()
    try:
        recommendations_db = Database.handle_student_submission(db, quiz_data)
        return ClubRecommendationResponse(recommendations=recommendations_db)
    finally:
        Database.close_database_connection(db)

@app.on_event("startup")
async def startup():
    global db
    db = Database.connect_to_database()

@app.on_event("shutdown")
async def shutdown():
    Database.close_database_connection(db)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #http://127.0.0.1:8000
