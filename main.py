from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Optional
from pydantic import BaseModel

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


# @app.get("/items")
# async def list_items(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


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


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
async def read_items(q: list[str] = Query(..., min_length=4, max_length=10, alias="item-query")):
    results = {"items": fake_items_db}
    if q:
        results.update({"q": q})
    return results


@app.get('/items_hidden')
async def hidden_query_route(hidden_query: str = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"hidden_query": "hidden_query not found"}


@app.get("/items_validation/{item_id}")
async def read_items_validation(*, item_id: int = Path(..., title="The ID of the item to get", ge=10),
                                q: str = Query("Hello")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
