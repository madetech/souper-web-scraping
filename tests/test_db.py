from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from models.basic import Report
from sqlalchemy.orm import Session
import random
import string
from services import db
from sqlalchemy import text
from services.db import souperDB

def test_dbConnection():
    connection = souperDB().get_connection()
    trans = connection.begin()
    try:
        connection.execute(text('SELECT 1'))
        trans.commit()
        assert True
    except Exception:
        trans.rollback()
        # print('\n\n----------- Connection failed ! ERROR : ', e)
        assert False
    
def test_db_insert_report():
    engine = souperDB().get_engine()
    random_str_dummy_name = ''.join(random.choices(string.ascii_letters))
    report = Report(assessment_date="today",
                overall_verdict="pass",
                name=random_str_dummy_name,
                url="www.")
    db.insert_entry(report, engine)
    result = Session(engine).query(Report).filter(Report.name==random_str_dummy_name).all()
    assert len(result) == 1
