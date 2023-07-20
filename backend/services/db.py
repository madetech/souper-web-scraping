from sqlalchemy import Connection, create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import URL
from models.basic import Report, Section, Base
from sqlalchemy.orm import Session

def insert_entry(entry: Base, engine):
    with Session(engine) as session:
        session.add(entry)
        session.commit()
    session.close()

def upsert_report(report: Report, conn: Connection):
    report_table = Report.__table__
    statement = insert(table).values(
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
            )
        ).returning(report_table.c["id"])

    for row in conn.execute(statement):
        report_id = row[0]
        
    sections = []
    for section in report.sections:
        sections.append({
            "report_id": report_id,
            "number": section.number,
            "decision": section.decision
        })

    # TODO: Update sections if already present using on_conflict_do_update
    statement = insert(Section.__table__).values(sections)
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