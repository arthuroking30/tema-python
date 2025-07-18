from models.User import User
from sqlmodel import Session, select
from schemas.user_create_schema import UserCreateRequest
from utils.jwt_utils import create_access_token
from sqlalchemy.exc import IntegrityError
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed


def create_user(req: UserCreateRequest, session: Session):
    # Hash the password before saving
    hashed_password = hash_password(req.password)
    user = User(
        username=req.username, email=req.email, password=hashed_password
    )
    session.add(user)
    session.commit()
    return user


def get_all_users(session: Session):
    return list(session.exec(select(User)))


def login_user(req: UserCreateRequest, session: Session):
    user = session.exec(select(User).where(User.email == req.email)).first()
    if not user:
        raise IntegrityError(None, None, "User not found")
    if not verify_password(req.password, user.password):
        raise IntegrityError(None, None, "Incorrect password")
    token = create_access_token({"sub": user.email, "username": user.username})
    return token
