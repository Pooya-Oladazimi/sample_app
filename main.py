from fastapi import FastAPI
import dotenv
import os

app = FastAPI()

dotenv.load_dotenv()

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
db_endpoint = os.environ.get("DB_ENDPOINT")


@app.get("/user")
def user():
    db_conn = f"postgresql://{db_user}:{db_pass}@{db_endpoint}:5432/{db_name}"
    return {"_result": "User says hello"}


@app.get("/post")
def post():
    return {"_result": "This is a Post."}


@app.get("/news")
def news():
    return {"_result": "This is the latest news."}
