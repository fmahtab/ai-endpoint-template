from fastapi import APIRouter
from app.schemas.ask import AskRequest, AskResponse
from app.services.reasoning import ReasoningService

router = APIRouter()

service = ReasoningService()

@router.post("/ask")
def ask_question(request: AskRequest) -> AskResponse:
    return service.answer_question(request.question)