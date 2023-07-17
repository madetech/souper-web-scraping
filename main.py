from typing import Union
from fastapi import FastAPI
from services.basic_info_scraper import get_all_reports, get_all_service_standard_links
from services.db import insert_entry, souperDB, upsert_report

app = FastAPI()
db = souperDB()

@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}


@app.get("/standard-reports")
def get_standard_reports():
    return get_all_service_standard_links()

@app.get("/scrape", status_code=201)
def scrape_report_data():
    report_data = get_all_reports()
    
    for report in report_data:
        upsert_report(report, db.getConnection())