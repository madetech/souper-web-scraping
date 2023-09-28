import logging
import os

from data import feedback_reader, report_reader, section_reader
from data.database import souperDB
from data.report_writer import upsert_reports
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_pagination import LimitOffsetPage, add_pagination
from models.report import ReportOut
from services.basic_info_scraper import scrape_reports
from sqlalchemy.orm import Session

load_dotenv()

logging.basicConfig(level=logging.INFO) # Change this to logging.DEBUG to see more detail in logs

app = FastAPI()
add_pagination(app)

# Block scrape until previous complete
app.is_scraping = False # type: ignore - VSCode complains about this but it should be a legal declaration
# https://github.com/tiangolo/fastapi/issues/592

db = souperDB()

origins = [os.getenv('REACT_APP_FRONTEND')]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get("/scrape", status_code=201)
def scrape_report_data(session: Session = Depends(db.get_session)):
    if not app.is_scraping: # type: ignore
        app.is_scraping = True # type: ignore
        report_data = scrape_reports()
        upsert_reports(report_data, session)
        app.is_scraping = False # type: ignore
        

@app.get("/reports", response_model=LimitOffsetPage[ReportOut])
def get_reports(database: Session = Depends(db.get_session)):
    return report_reader.get_reports(database)


@app.get("/reports/{id}/sections")
def get_sections(id, database: Session = Depends(db.get_session)):
    return section_reader.get_sections(id, database)


@app.get("/sections/{id}/feedback")
def get_feedback(id, database: Session = Depends(db.get_session)):
    return feedback_reader.get_feedback(id, database)
