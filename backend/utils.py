import os
import jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

# initalize the password hashing context with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Read the secret key from an environment variable (with a fallback for development)
SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a given hashed password.

    Args:
        plain_password (str): The plaintext password.
        hashed_password (str): The hashed password.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta=None) -> str:
    """
    Create a JWT access token for a user.

    Args:
        data (dict): A dictionary containing the data to include in the token payload.
        expires_delta (timedelta, optional): The amount of time before the token expires, as a timedelta.
            Defaults to ACCESS_TOKEN_EXPIRE_MINUTES minutes if not provided.

    Returns:
        str: The encoded JWT token
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt