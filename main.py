from fastapi import FastAPI

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