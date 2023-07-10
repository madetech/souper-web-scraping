from typing import Union
from fastapi import FastAPI
from first_pass import first_pass

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/firstPass")
def do_first_pass():
    return first_pass()