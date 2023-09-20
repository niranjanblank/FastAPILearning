from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world 2"}


@app.post("/")
async def post():
    return {"message": "This is a post route"}


@app.put("/")
async def put():
    return {"message": "This is a put route"}


@app.get("/users")
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"message": "This is the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"message": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {
            "food_name": food_name,
            "message": "you are healthy"
        }

    if food_name.value == 'fruits':
        return {
            "food_name": food_name,
            "message": "you are healthy, but you are a fruit"
        }

    return {
        "food_name": food_name,
        "message": "this is a dairy product"
    }


# query params
fake_items_db = [
    {'item_name': 'item 1'},
    {'item_name': 'item 2'},
    {'item_name': 'item 3'},
    {'item_name': 'item 4'},
    {'item_name': 'item 5'},
    {'item_name': 'item 6'},
    {'item_name': 'item 7'},
    {'item_name': 'item 8'},
    {'item_name': 'item 9'},
    {'item_name': 'item 10'}
]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum"})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum"})
    return item
