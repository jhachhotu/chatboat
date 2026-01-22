from pymongo import MongoClient

class MongoDB:
    _client = None

    @classmethod
    def get_client(cls):
        if not cls._client:
            cls._client = MongoClient("mongodb://localhost:27017")
        return cls._client

    @classmethod
    def get_db(cls):
        return cls.get_client()["job_chatbot_db"]
