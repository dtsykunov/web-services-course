from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {}


class Item(BaseModel):
    name: str
    price: float


DISCOUNT = 0.15


@app.get("/")
async def hard_coded():
    return "some hard coded data"


@app.post("/item")
async def item_post(item: Item):
    items[item.name] = item
    return {
        "name": item.name + " (with discount)",
        "price": item.price * (1 - DISCOUNT)
    }


@app.get("/item/{name}")
async def item_get(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="item not found")
    return items[name]
