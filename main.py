from typing import Union
from fastapi import FastAPI
from services.basic_info_scraper import get_all_service_standard_links

app = FastAPI()


@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}


@app.get("/standard-reports")
def get_standard_reports():
    return get_all_service_standard_links()
