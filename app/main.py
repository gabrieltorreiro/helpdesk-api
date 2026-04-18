from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import auth, user

app = FastAPI(title="HelpDesk API")

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "HelpDesk API is running"}