from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    text: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{id}", response_model=Item)
async def read_item(id: int) -> Item:
    items = [Item(id = 1, text = "good"), Item(id = 2, text = "bad")]
    foundItem = [item for item in items if item.id == id]
    return foundItem[0]
