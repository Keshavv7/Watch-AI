from fastapi import APIRouter, Depends
from services.gpt3_service import generate_responses

router = APIRouter()

@router.post("/generate_response/")
async def generate_response(prompt: str):
    response = generate_responses(prompt)
    
    return {"response": response}
