from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, Gal Sarig 3", "message": "Welcome to FastAPI! I've changed this line :)"}
