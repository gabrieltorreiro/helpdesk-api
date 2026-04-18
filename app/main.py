from fastapi import FastAPI
from app.routes import user

app = FastAPI(title="HelpDesk API")

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "HelpDesk API is running"}