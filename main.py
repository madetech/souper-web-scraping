from fastapi import FastAPI
from services.basic_info_scraper import get_all_reports
from services.db import souperDB, upsert_report

app = FastAPI()
db = souperDB()

@app.get("/alive", status_code=200)
async def alive():
    return {"Me": "Hi"}

@app.get("/scrape", status_code=201)
def scrape_report_data():
    report_data = get_all_reports()
    
    for report in report_data:
        upsert_report(report, db.getConnection())