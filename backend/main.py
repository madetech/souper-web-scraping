from data import report_reader
from data.database import souperDB
from data.report_writer import upsert_report
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import LimitOffsetPage, add_pagination
from models.report import ReportOut
from services.basic_info_scraper import scrape_reports
from sqlalchemy import Engine

load_dotenv()

app = FastAPI()
add_pagination(app)

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
    report_data = scrape_reports()
    
    for report in report_data:
        upsert_report(report, db.get_connection())

@app.get("/reports", response_model=LimitOffsetPage[ReportOut])
def get_reports(database: Engine = Depends(db.get_engine)):
    return report_reader.get_reports(database)