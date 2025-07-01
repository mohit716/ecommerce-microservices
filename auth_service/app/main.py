from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

app = FastAPI(
    title="Auth Microservice",
    description="Handles user authentication for the e-commerce system",
    version="1.0.0"
)


app.include_router(auth_router, prefix="/api/auth")
