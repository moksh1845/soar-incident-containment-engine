from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi import status

from app.models.user import User

from app.schemas.user import UserCreate

from app.repositories.user_repository import UserRepository

from app.core.security import hash_password
from app.core.security import verify_password

from app.core.jwt_handler import create_access_token


class AuthService:

    @staticmethod
    def register(
        db: Session,
        user_data: UserCreate
    ):

        existing_user = UserRepository.get_by_username(
            db,
            user_data.username
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        existing_email = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hash_password(
                user_data.password
            ),
            role_id=user_data.role_id
        )

        return UserRepository.create_user(
            db,
            user
        )

    @staticmethod
    def login(
        db: Session,
        username: str,
        password: str
    ):

        user = UserRepository.get_by_username(
            db,
            username
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "username": user.username
            }
        )

        return token