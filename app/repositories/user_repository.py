from app.core.database import MongoDB
from app.models.user import User

class UserRepository:
    def __init__(self):
        self.collection = MongoDB.get_db()["users"]

    def find_by_email(self, email: str):
        return self.collection.find_one({"email": email})

    def create(self, user: User):
        self.collection.insert_one(user.to_dict())
