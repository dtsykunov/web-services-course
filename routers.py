from fastapi import APIRouter, HTTPException, Depends

from models import Item, Category, Store

store_router = APIRouter(prefix="/store")

_store = Store()


async def get_store():
    return _store


@store_router.get("/", response_model=Store)
async def stock_get(store: Store = Depends(get_store)):
    return store


@store_router.post("/{category_name}", response_model=Item)
async def add_to_stock(category_name: str,
                       item: Item,
                       store: Store = Depends(get_store)):
    store.add_to_stock(category_name, item)
    return item


@store_router.get("/{category_name}/{item_name}", response_model=list[Item])
async def items_in_stock(category_name: str,
                         item_name: str,
                         store: Store = Depends(get_store)):
    if not store.contains(category_name, item_name):
        raise HTTPException(status_code=404, detail="not found")
    return store.get_items(category_name, item_name)
