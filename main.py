from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, MICHAL", "message": "Welcome to FastAPI! I've changed this line :)"}
