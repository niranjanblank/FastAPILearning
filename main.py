from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello world 2"}

@app.post("/")
async def post():
    return {"message": "This is a post route"}

@app.put("/")
async def put():
    return {"message": "This is a put route"}

@app.get("/users")
async def list_items():
    return {"message": "list users route"}

@app.get("/users/me")
async def get_current_user():
    return {"message": "This is the current user"}
@app.get("/users/{user_id}")
async def get_item(user_id: str):
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