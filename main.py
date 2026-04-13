from fastapi import FastAPI

app = FastAPI()


@app.get("/user")
def user():
    return {"_result": "User says hello"}


@app.get("/post")
def post():
    return {"_result": "This is a Post."}
