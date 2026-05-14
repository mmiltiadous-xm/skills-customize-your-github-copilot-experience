# Starter code for Building REST APIs with FastAPI

# 1. Install FastAPI and Uvicorn before running:
#    pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Example Pydantic model
data_store: Dict[int, dict] = {}

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

# Add your CRUD endpoints below
