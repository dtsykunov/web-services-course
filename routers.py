from fastapi import APIRouter, HTTPException

from models import Item

items = {}

DISCOUNT = 0.15

items_router = APIRouter(prefix="/items")


@items_router.get("/")
async def items_readall():
    return items


@items_router.post("/item", response_model=Item)
async def item_post(item: Item):
    items[item.name] = item
    return {
        "name": item.name + " (with discount)",
        "price": item.price * (1 - DISCOUNT)
    }


@items_router.get("/{name}", response_model=Item)
async def item_get(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="item not found")
    return items[name]
