from fastapi import FastAPI

app = FastAPI(title="HelpDesk API")

@app.get("/")
def root():
    return {"message": "HelpDesk API is running"}