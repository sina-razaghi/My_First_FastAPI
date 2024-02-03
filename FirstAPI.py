from anyio import Path
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/login/{user_id}")
async def read(user_id: int):
    return {"id" : user_id,
            "username": "username",
            "message": "Welcome to home"
            }

@app.post("/results")
async def results():
    return {"detail": "Somethings about app"}
