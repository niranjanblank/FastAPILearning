from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello world 2"}

@app.post("/")
async def post():
    return {"message": "This is a post route"}
