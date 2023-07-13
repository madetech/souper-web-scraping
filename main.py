from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from services.first_pass import first_pass

load_dotenv()

app = FastAPI()


@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}


@app.get("/firstPass")
def do_first_pass():
    return first_pass()
