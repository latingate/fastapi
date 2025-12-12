from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, Gal Sarig 2!", "message": "Welcome to FastAPI! I've changed this line :)"}
