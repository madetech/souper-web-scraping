from models.report import Base, Report
from sqlalchemy import Connection
from sqlalchemy.dialects.postgresql import insert
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