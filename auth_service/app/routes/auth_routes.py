from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister
from app.core.security import hash_password

router = APIRouter()

# In-memory store (mock DB)
mock_users = []

@router.get("/health")
def health_check():
    return {"status": "Auth service is healthy"}

@router.post("/register")
def register_user(user: UserRegister):
    # Check if user already exists
    for u in mock_users:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user.password)
    user_dict = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pwd,
    }
    mock_users.append(user_dict)
    return {"message": "User registered successfully"}
