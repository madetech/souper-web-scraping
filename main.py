from typing import Union
from fastapi import FastAPI
from services.first_pass import first_pass
from fastapi.middleware.cors import CORSMiddleware
import os
# from dotenv import load_dotenv

# load_dotenv()

# POSTGRES_USER = os.getenv('POSTGRES_USER')
# POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# POSTGRES_DB = os.getenv('POSTGRES_DB')

# print(POSTGRES_USER)

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}

@app.get("/report", status_code=200)
async def list_report():
    return [{"id": "12", "assessment_date": "14/06/2023", "name": "anna", "overall_verdict": "pass"}, {"id": "13", "assessment_date": "13/06/2023", "name": "rose", "overall_verdict": "pass"}]


@app.get("/firstPass")
def do_first_pass():
    return first_pass()
