from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get("/", description="This is get route", deprecated=True)

async def root():
    return {"message": "Hello world"}


@app.post("/", description="This is post route")

async def post():
    return {"message": "Hello from post"}

@app.put("/")
async def put():
    return {"message": "Hello from put"}

@app.get("/users")
async def get():
    return {"message" : "list items"}

@app.get("/users/{user_id}")
async def get_item(user_id: str):
    return {"user_id": user_id}

@app.get("/user/me")
async def get_current_user():
    return {"Message" : "This is current user"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name" : food_name, "message": "You are healthy"}
    if food_name.value == 'fruits':
        return {
            "food_name": food_name, 
            "message": "You are still health but like sweet things"
            }
    return {"food_name": food_name, "message": "i like chocolate milk"}