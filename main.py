from datetime import datetime, time

from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl
from uuid import UUID
app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "hello world 2"}
#
#
# @app.post("/")
# async def post():
#     return {"message": "This is a post route"}
#
#
# @app.put("/")
# async def put():
#     return {"message": "This is a put route"}
#
#
# @app.get("/users")
# async def list_users():
#     return {"message": "list users route"}
#
#
# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "This is the current user"}
#
#
# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"message": user_id}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {
#             "food_name": food_name,
#             "message": "you are healthy"
#         }
#
#     if food_name.value == 'fruits':
#         return {
#             "food_name": food_name,
#             "message": "you are healthy, but you are a fruit"
#         }
#
#     return {
#         "food_name": food_name,
#         "message": "this is a dairy product"
#     }
#
#
# # query params
# fake_items_db = [
#     {'item_name': 'item 1'},
#     {'item_name': 'item 2'},
#     {'item_name': 'item 3'},
#     {'item_name': 'item 4'},
#     {'item_name': 'item 5'},
#     {'item_name': 'item 6'},
#     {'item_name': 'item 7'},
#     {'item_name': 'item 8'},
#     {'item_name': 'item 9'},
#     {'item_name': 'item 10'}
# ]
#
#
# # @app.get("/items")
# # async def list_items(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum"})
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum"})
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({'price_with_tax': price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items")
# async def read_items(q: list[str] = Query(..., min_length=4, max_length=10, alias="item-query")):
#     results = {"items": fake_items_db}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: str = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "hidden_query not found"}
#
#
# @app.get("/items_validation/{item_id}")
# async def read_items_validation(*, item_id: int = Path(..., title="The ID of the item to get", ge=10),
#                                 q: str = Query("Hello")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

"""
Body Multiple Parameters
"""


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None


# @app.put("/items/{item_id}")
# async def update_item(
#         *, item_id: int = Path(..., title='The Id of the item to get'),
#         q: str | None = None,
#         item: Item = Body(..., embed=True),
#         user: User | None = None,
#         importance: int = Body(...)
# ):
#     results = {
#         "item_id": item_id
#     }
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     if importance:
#         results.update({"importance": importance})
#     return results


# class Item(BaseModel):
#     name: str
#     description: str = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(...,
#                          gt=10, description='The price must be grater tan zero'
#                          )
#     tax: float = None
# @app.put('/items/{item_id')
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# nested models

# class Image(BaseModel):
#     # url: str = Field(..., pattern='^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$')
#     url: HttpUrl
#     name: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None= None
#     price: float
#     tax: float | None=None
#     tags: list[str] = []
#     image: Image | None = None
#
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, 'item': item}
#     return results

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class Item(BaseModel):
#     name: str = Field(..., example="Foo")
#     description: str = Field(None, example="Description of item")
#     price: float = Field(..., example=16.25)
#     tax: float = Field(None, example=1.25)
# class Config:
#     json_schema_extra = {
#         "example": {
#             "name": "Foo",
#             "description": "Description of this item",
#             "price": 14.25,
#             "tax": 2.25
#         }
#     }

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., example={
#     "name": "Foo",
#     "description": "Description of this item",
#     "price": 14.25,
#     "tax": 2.25
# })):
#     results = {"item_id": item_id, "item": item}
#     return results

#extra data types
# @app.put("/items/{item_id}")
# async def read_items(item_id: UUID, start_date: datetime = Body(None),
#                      end_date: datetime = Body(None),
#                      repeat_at: time = Body(None)
#                      ):
#     results = {"item_id": item_id, "start_date": start_date, "end_date": end_date}
#     return results

# cookie and header

@app.get("/items")
async def read_items(cookie_id: str = Cookie(None),
                     accept_encoding: str = Header(None)
                     ):
    return {"cookie_id": cookie_id, "Accept-Encoding": accept_encoding}