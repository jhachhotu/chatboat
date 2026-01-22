from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    message: str

class ChatMessageResponse(BaseModel):
    reply: str

class ChatHistoryResponse(BaseModel):
    messages: list[ChatMessageResponse]


