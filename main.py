from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/item/")
async def read_item(name: str = "undefined"):
    return {"message": f"Item {name}"}


@app.post("/items")
async def store_item(item: Item):
    return item
