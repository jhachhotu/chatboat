
from datetime import datetime

class Message:
    def __init__(self, user_id: str, text: str):
        self.user_id = user_id
        self.text = text
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "text": self.text,
            "timestamp": self.timestamp
        }
