from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from models.basic import Report
from sqlalchemy.orm import Session
import random
import string
from models import db



url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="postgres"
    )
engine = create_engine(url)
    
def test_db_insert_report():
    random_str_dummy_name = ''.join(random.choices(string.ascii_letters))
    report = Report(assessment_date="today",
                overall_verdict="pass",
                name=random_str_dummy_name,
                url="www.")
    db.insert_entry(report, engine)
    result = Session(engine).query(Report).filter(Report.name==random_str_dummy_name).all()
    assert len(result) == 1
