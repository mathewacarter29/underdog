"""
API driver file
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    main get endpoint
    """
    return {"message": "Hello World"}
