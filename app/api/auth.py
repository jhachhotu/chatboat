from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(req: RegisterRequest):
    try:
        auth_service.register(req.email, req.password)
        return {"message": "User registered"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest):
    try:
        token = auth_service.login(req.email, req.password)
        return TokenResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
