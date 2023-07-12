from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from basic import Report, Section

from sqlalchemy.orm import Session

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="postgres"
)

engine = create_engine(url)

report = Report(assessment_date="today",
                overall_verdict="pass",
                name="anna",
                url="www.")

#now connect
connection = engine.connect()
with Session(engine) as session:
    session.add(report)
    session.commit()