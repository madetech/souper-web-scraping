from typing import Union
from fastapi import FastAPI
from first_pass import first_pass
import os
# from dotenv import load_dotenv

# load_dotenv()

# POSTGRES_USER = os.getenv('POSTGRES_USER')
# POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# POSTGRES_DB = os.getenv('POSTGRES_DB')

# print(POSTGRES_USER)

app = FastAPI()


@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}


@app.get("/firstPass")
def do_first_pass():
    return first_pass()
