# 🤖 AI Chatbot API

A production-ready AI Chatbot backend built with **FastAPI**, designed for fast, scalable, and secure conversational AI applications. The project provides REST APIs for managing conversations, generating AI responses, handling authentication, storing chat history, and supporting modern chatbot workflows.

---

## 🚀 Features

- ⚡ High-performance FastAPI backend
- 🤖 AI-powered chatbot responses
- 💬 Conversation & chat history management
- 🔐 JWT Authentication & Authorization
- 👤 User registration & login
- 📂 Conversation management
- 📝 Message persistence
- 🔄 Async API endpoints
- 🗄️ PostgreSQL database support
- 📦 SQLAlchemy ORM
- 🔄 Alembic database migrations
- 📖 Automatic Swagger & ReDoc documentation
- 🔒 Password hashing using Argon2
- 🌍 CORS support
- ⚙️ Environment-based configuration
- 🐳 Docker-ready architecture
- 📈 Scalable and production-friendly design

---

## 🏗️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python 3.13+ |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Hashing | Argon2 |
| Validation | Pydantic |
| Migrations | Alembic |
| ASGI Server | Uvicorn |
| Package Manager | uv |
| API Documentation | Swagger UI & ReDoc |

---

## 📁 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── auth/
│   ├── chatbot/
│   ├── config/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── dependencies/
│   └── main.py
│
├── alembic/
├── migrations/
├── tests/
├── .env
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot-backend.git

cd chatbot-backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Using pip

```bash
pip install -r requirements.txt
```

or using uv

```bash
uv sync
```

---

## 4. Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost/chatbot_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

OPENAI_API_KEY=your_api_key
```

---

## 5. Run Database Migrations

```bash
alembic upgrade head
```

---

## 6. Start the Server

```bash
uvicorn app.main:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

Interactive documentation is automatically generated.

### Swagger UI

```
http://localhost:8000/docs
```

### ReDoc

```
http://localhost:8000/redoc
```

---

# 🔑 Authentication

The API uses **JWT Authentication**.

Workflow:

1. Register a new account
2. Login
3. Receive an access token
4. Include the token in API requests

```
Authorization: Bearer <your_token>
```

---

# 💬 Core Functionalities

### User Authentication

- Register
- Login
- Logout
- Refresh Token
- Protected Routes

---

### Chatbot

- Create conversation
- Send message
- Receive AI response
- Retrieve conversation history
- Continue existing conversations
- Delete conversations

---

### User Management

- User Profile
- Update Profile
- Password Security
- Authentication

---

### Conversation Management

- Create Conversation
- List Conversations
- Fetch Messages
- Delete Conversation
- Store Chat History

---

# 🛡️ Security Features

- JWT Authentication
- Password Hashing (Argon2)
- Environment Variables
- SQL Injection Protection
- Input Validation
- CORS Protection
- Secure Password Storage

---

# 🗄️ Database

The project uses **PostgreSQL** with **SQLAlchemy ORM** and **Alembic** for schema migrations.

Example workflow:

```bash
alembic revision --autogenerate -m "Initial Migration"

alembic upgrade head
```

---

# 🚀 Deployment

The project can be deployed using:

- Docker
- Render
- Railway
- Fly.io
- AWS EC2
- DigitalOcean
- Azure
- Google Cloud Platform

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📦 Dependencies

Some of the major packages used:

- FastAPI
- SQLAlchemy
- AsyncPG
- Alembic
- Pydantic
- Uvicorn
- Argon2
- python-jose
- passlib
- email-validator
- Celery *(optional for background tasks)*

---

# 📈 Future Improvements

- Streaming AI responses
- Voice conversations
- Multi-model AI support
- Image generation
- File uploads
- Chat summarization
- Conversation search
- WebSocket support
- Rate limiting
- Redis caching
- Background task processing
- Admin dashboard
- Analytics

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Your Name**

- GitHub: https://github.com/jhachhotu
- LinkedIn: https://www.linkedin.com/in/kumarchhotu/

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
