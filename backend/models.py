"""
models.py

This module defines the ORM models for the Event Logger App using SQLAlchemy.
It includes models for User, Event, and EventOccurrence which represent the core
database tables and their relationships.

Classes:
    User: Represents a user in the system.
    Event: Represent a specific event type associated with a user.
    EventOccurrence: Logs an occurrence of an event with a timestamp.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

from datetime import datetime
from typing import List

from database import Base


# User model represents the application's users.
class User(Base):
    """User model for representing application users."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password_hash: Mapped[str]

    # One-to-many relationship: A user can have multiple events.
    events: Mapped[List["Event"]] = relationship(
        back_populates="user", cascade="all, delete"
    )


class Event(Base):
    """Event model for representing an event type."""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    event_name: Mapped[str] = mapped_column(index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="events")
    occurrences: Mapped["EventOccurrence"] = relationship(
        back_populates="event", cascade="all, delete"
    )


class EventOccurrence(Base):
    """EventOccurrence model for logging individual occurrences of an event."""

    __tablename__ = "event_occurrences"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    timestamp: Mapped[datetime] = mapped_column(default=func.now())

    event: Mapped["Event"] = relationship(back_populates="occurrences")
