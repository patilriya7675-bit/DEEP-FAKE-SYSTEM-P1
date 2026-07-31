from fastapi import APIRouter, HTTPException, status, Request
from pydantic import BaseModel

from backend.security.password import (
    hash_password,
    verify_password
)

from backend.security.jwt_handler import (
    create_access_token
)

from backend.security.rate_limiter import limiter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class LoginRequest(BaseModel):
    username: str
    password: str


# Fake database (temporary)
fake_users = {
    "pratik": {
        "password": hash_password("Pratik@123"),
        "role": "admin"
    },
    "riya": {
        "password": hash_password("Riya@123"),
        "role": "analyst"
    },
    "guest": {
        "password": hash_password("Guest@123"),
        "role": "user"
    }
}


@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, data: LoginRequest):
    """
    Authenticate user and return JWT token.
    """

    # Check if username exists
    if data.username not in fake_users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username"
        )

    user = fake_users[data.username]

    # Verify password
    if not verify_password(
        data.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    # Create JWT token
    token = create_access_token(
        {
            "sub": data.username,
            "role": user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }