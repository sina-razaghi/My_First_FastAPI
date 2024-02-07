from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/home")
async def home():
    return {"message": "Home Page"}


@app.get("/login/{user_id}")
async def read(user_id: int):
    return {"id" : user_id,
            "username": "username",
            "message": "Welcome to home"
            }


@app.get("/users")
async def users():
    return {"list": ["Rick", "Morty", "John"]}


@app.get("/panel")
async def panel():
    return {"id": "admin"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residauls"}


@app.get("/results")
async def results():
    return {"detail": "Somethings about app"}
