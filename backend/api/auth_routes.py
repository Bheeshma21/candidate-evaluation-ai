from fastapi import APIRouter, HTTPException

from database.database import SessionLocal

from schemas.user_schema import UserRegister, UserLogin

from repositories.user_repository import UserRepository

from auth.security import hash_password, verify_password
from auth.jwt_handler import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(request: UserRegister):

    db = SessionLocal()

    try:

        existing_user = UserRepository.get_by_email(
            db,
            request.email
        )

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        user = UserRepository.create(
            db=db,
            full_name=request.name,
            email=request.email,
            password=hash_password(request.password)
        )

        return {
            "message": "User registered successfully",
            "user_id": user.id
        }

    finally:

        db.close()


@router.post("/login")
def login(request: UserLogin):

    db = SessionLocal()

    try:

        user = UserRepository.get_by_email(
            db,
            request.email
        )

        if user is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            request.password,
            user.password
        ):

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    finally:

        db.close()