from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.core.security import hash_password, verify_password

router = APIRouter()

# In-memory mock user storage (for demo purposes only)
mock_users = []

# Health check endpoint
@router.get("/health")
def health_check():
    return {"status": "Auth service is healthy"}

# Register endpoint
@router.post("/register")
def register_user(user: UserRegister):
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

# Login endpoint
@router.post("/login")
def login_user(user: UserLogin):
    for u in mock_users:
        if u["email"] == user.email:
            if verify_password(user.password, u["hashed_password"]):
                return {"message": "Login successful"}
            else:
                raise HTTPException(status_code=401, detail="Invalid credentials")
    raise HTTPException(status_code=404, detail="User not found")
