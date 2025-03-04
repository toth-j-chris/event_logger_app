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

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


# User model represents the application's users.
class User(Base):
    """User model for representing application users."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(*String, unique=True, index=True)
    password_hash = Column(String)

    # One-to-many relationship: A user can have multiple events.
    events = relationship("Event", back_populates="owner", cascade="all, delete")


class Event(Base):
    """Event model for representing an event type."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="events")
    occurrences = relationship(
        "EventOccurrence", back_populates="event", cascade="all, delete"
    )


class EventOccurrence(Base):
    """EventOccurrence model for logging individual occurrences of an event."""

    __tablename__ = "event_occurrences"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    event = relationship("Event", back_populates="occurrences")
