import logging
import os
from data.tables import feedback_response_summary
from data.charts import counts_by_result_type
from data.charts import average_by_result_type
from data import feedback_reader, report_reader, section_reader
from data.database import souperDB
from data.report_writer import upsert_reports
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from models.report import ReportOut
from services.basic_info_scraper import scrape_reports
from sqlalchemy.orm import Session

load_dotenv()

logging.basicConfig(level=logging.INFO) # Change this to logging.DEBUG to see more detail in logs

app = FastAPI()


# Block scrape until previous complete
app.is_scraping = False # type: ignore - VSCode complains about this but it should be a legal declaration
# https://github.com/tiangolo/fastapi/issues/592

db = souperDB()
logging.info(f"Database connection at {db}, status {db.get_connection}")

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
        

@app.get("/reports", response_model=list[ReportOut])
def get_reports(database: Session = Depends(db.get_session)):
    return report_reader.get_reports(database)


@app.get("/reports/{id}/sections")
def get_sections(id, database: Session = Depends(db.get_session)):
    return section_reader.get_sections(id, database)


@app.get("/sections/{id}/feedback")
def get_feedback(id, database: Session = Depends(db.get_session)):
    return feedback_reader.get_feedback(id, database)


@app.get("/datacounts")
def get_graph_data_count(session:Session = Depends(db.get_session)):
    return counts_by_result_type.get_result_type_counts(session)


@app.get("/dataaverage")
def get_graph_data_average(session:Session = Depends(db.get_session)):
    return average_by_result_type.get_result_type_averages(session)

@app.get("/resultcount")
def get_chart_result_count(session:Session = Depends(db.get_session)):
    logging.error('backend triggered')
    return feedback_response_summary.get_results_summary_count(session)
