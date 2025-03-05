from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.database import get_db
from backend.models import User
from backend.schemas import UserCreate, UserResponse
from backend.utils import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Register a new user.

    This endpoint registers a new user by validating the input,
    hashing the password, and saving the user to the database.

    Args:
        user (UserCreate): The user registration information.
        db (AsyncSession): The database session provided by the get_db dependency.

    Returns:
        UserResponse: The created user data.

    Raises:
        HTTPException: If the username is already taken.
    """
    query = select(User).where(User.username == user.username)
    result = await db.execute(query)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
        )

    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, password_hash=hashed_pw)
    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return new_user


@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Log in a user and return an access token.

    This endpoint verifies the user's credentials and returns a JWT token
    if the credentials are valid.

    Args:
        user (UserCreate): The user's login credentials.
        db (AsyncSession): The database session provided by the get_db dependency.

    Returns:
        dict: A dictionary containing the access token and its type.

    Raises:
        HTTPException: If the credentials are invalid.
    """
    query = select(User).where(User.username == user.username)
    result = await db.execute(query)
    db_user = result.scalars().first()

    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    token = create_access_token({"sub": db_user.usernmae})

    return {"access token": token, "token_type": "bearer"}
