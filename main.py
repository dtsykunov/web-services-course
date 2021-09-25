from fastapi import FastAPI
from routers import items_router

app = FastAPI()

app.include_router(items_router)


@app.get("/")
async def hard_coded():
    return "some hard coded data"
