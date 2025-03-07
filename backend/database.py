"""
database.py

This module sets up the asynchronous SQLAlchemy engine and session for the Event Logger App.
It also provides a dependency for FastAPI endpoints to obtain a database session.

Attributes:
    DATABASE_URL (str): The database connection URL loaded from the environment.
    engine (AsyncEngine): The SQLAlchemy asynchronous engine.
    async_session (sessionmaker): A session factory for creating asynchronous sessions.
    Base (DeclarativeMeta): The declarative base class used fro defining ORM models.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def get_db():
    """Provides a database session to FastAPI endpoints.

    This dependency function yields an asynchronous SQLAlchemy session
    which is automatically closed after the request is completed.

    Yields:
        AsyncSession: An active database session.
    """
    async with async_session() as session:
        yield session
