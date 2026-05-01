from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simple In-Memory Data for demonstration
class Item(BaseModel):
    id: int
    name: str
    price: float

items_db = []

# CREATE: Add a new item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items_db.append(item)
    return item

# READ: Get all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    return items_db

# UPDATE: Modify an existing item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE: Remove an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
