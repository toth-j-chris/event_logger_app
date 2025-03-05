"""
schemas.py

This module defines the Pydantic schemas for the Event Logger App. These schemas are used
to validate incoming API requests and format outgoing responses. They also enable automatic
serialization of ORM objects via Pydantic's configuration.

Schemas:
    UserCreate: Schema for creating a new user.
    UserResponse: Schema for returning user data.
    EventCreate: Schema for creating a new event.
    EventRespone: Schema for returning event data.
    EventOccurrenceCreate: Schema for creating a new event occurrence.
    EventOccurrenceResponse: Schema for returning event occurrence data.
"""
from pydantic import BaseModel, ConfigDict
from datetime import datetime

# --- User Schemas ---

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)

# --- Event Schemas ---

class EventCreate(BaseModel):
    event_name: str

class EventResponse(BaseModel):
    id: int
    event_name: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)

# --- Event Occurrence Schemas ---

class EventOccurrenceCreate(BaseModel):
    event_id: int

class EventOccurrenceResponse(BaseModel):
    id: int
    event_id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)