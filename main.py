from fastapi import FastAPI
from routers import store_router

app = FastAPI()

app.include_router(store_router)


@app.get("/")
async def hard_coded():
    return "some hard coded data"
