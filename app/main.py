from fastapi import FastAPI
from app.api import auth, chat
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

app = FastAPI()

user_repo = UserRepository()
auth_service = AuthService(user_repo)

app.include_router(auth.router)
app.include_router(chat.router)
