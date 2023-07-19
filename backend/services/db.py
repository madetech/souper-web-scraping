from sqlalchemy import Connection, create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import URL
from models.basic import Report, Base
from sqlalchemy.orm import Session

def insert_entry(entry: Base, engine):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
    session.close()

def upsert_report(report: Report, conn: Connection):
    statement = insert(Report.__table__).values(
            assessment_date=report.assessment_date,
            overall_verdict=report.overall_verdict,
            name=report.name,
            url=report.url,
            stage=report.stage
        ).on_conflict_do_update(
            constraint="report_url_key",
            set_=dict(
                overall_verdict=report.overall_verdict,
                stage=report.stage,
                assessment_date=report.assessment_date
            ))
        
    conn.execute(statement)
    conn.commit()
    conn.close()

class souperDB:
     
     # a method for printing data members
     def getConnection(self):
         DATABASE_URL = URL.create(
            drivername="postgresql",
            username="postgres",
            password="password",
            host="localhost",
            database="postgres"
        )

         engine = create_engine(DATABASE_URL, pool_pre_ping=False)
         return engine.connect()