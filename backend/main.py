from fastapi import FastAPI

from auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def read_root():
    return {"message": "Hello, Event Logger!"}