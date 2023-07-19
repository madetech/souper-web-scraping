from fastapi import FastAPI
from services.basic_info_scraper import get_reports
from services.db import souperDB, upsert_report
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = souperDB()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape", status_code=201)
def scrape_report_data():
    report_data = get_reports()
    
    for report in report_data:
        upsert_report(report, db.getConnection())

@app.get("/report", status_code=200)
async def list_report():
    return [{"id": "12", "assessment_date": "14/06/2023", "name": "anna", "overall_verdict": "pass"}, {"id": "13", "assessment_date": "13/06/2023", "name": "rose", "overall_verdict": "pass"}]
