from fastapi import FastAPI
from pydantic import BaseModel
from .schemas import QuizResponse, ClubRecommendationResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/submit_quiz", response_model=ClubRecommendationResponse)
def submit_quiz(response: QuizResponse):
    # Mock logic for processing answers and generating recommendations
    recommended_clubs = ["Women in Computer Science", "FIU Sustainability Club", "Volleyball Club", "Panther Robotics"]
    # Create the response message
    response_message = "Based on your answers, we recommend these clubs to enhance your student life at FIU."
    return ClubRecommendationResponse(
        message=response_message,
        recommendations=recommended_clubs
    )


@app.get("/clubs")
def get_clubs():
    # Mock data for available clubs
    # This could be replaced with a database query in the future
    clubs = [
        {"id": 1, "name": "Women in Computer Science"},
        {"id": 2, "name": "FIU Sustainability Club"},
        {"id": 3, "name": "Volleyball Club"},
        {"id": 4, "name": "Panther Robotics"},
    ]
    return {"clubs": clubs}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    #http://127.0.0.1:8000
