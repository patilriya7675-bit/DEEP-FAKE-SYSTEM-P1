from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from backend.security.password import (
    hash_password,
    verify_password
)

from backend.security.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class LoginRequest(BaseModel):
    username: str
    password: str


fake_user = {
    "username": "pratik",
    "password": hash_password("Pratik@123"),
    "role": "admin"
}


@router.post("/login")
def login(data: LoginRequest):

    if data.username != fake_user["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username"
        )

    if not verify_password(
        data.password,
        fake_user["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "sub": data.username,
            "role": fake_user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }