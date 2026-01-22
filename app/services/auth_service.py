from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register(self, email, password):
        if self.user_repo.find_by_email(email):
            raise Exception("User already exists")

        user = User(email, hash_password(password))
        self.user_repo.create(user)

    def login(self, email, password):
        user = self.user_repo.find_by_email(email)
        if not user or not verify_password(password, user["hashed_password"]):
            raise Exception("Invalid credentials")

        return create_access_token({"sub": user["email"]})
