# Event Logger App

Inital setup:
    Create a virtual environment:
        python3 -m venv venv
    Activate venv:
        source venv/bin/activate
    Install dependencies:
        pip install -r backend/requirements.txt
    
Start FastAPI backend by running while in the backend directory:
uvicorn main:app --reload

For in-memory MySQL db, use this in .env:
DATABASE_URL=sqlite+aiosqlite:///:memory: