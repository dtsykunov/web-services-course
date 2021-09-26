from fastapi import FastAPI
from routers import store_router
from graphene_schema import schema
from starlette.graphql import GraphQLApp

app = FastAPI()

app.include_router(store_router)
app.add_route("/graphql", GraphQLApp(schema=schema))


@app.get("/")
async def hard_coded():
    return "some hard coded data"
