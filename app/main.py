from fastapi import FastAPI
from app.database.connection import Base, engine
from app.routes import auth, user, ticket, comment


app = FastAPI(title="HelpDesk API")

# Base.metadata.create_all(bind=engine) # Uncomment this line the first time to create all tables in your database.
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(ticket.router)
app.include_router(comment.router)

@app.get("/")
def root():
    return {"message": "HelpDesk API is running"}