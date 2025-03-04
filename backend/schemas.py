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