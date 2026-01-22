from fastapi import APIRouter, Depends
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.core.auth_dependency import get_current_user

router = APIRouter(prefix="/chat")

@router.post("/")
def chat(req: ChatRequest, user=Depends(get_current_user)):
    reply = chat_service.process(req.message, user)
    return ChatResponse(reply=reply)
