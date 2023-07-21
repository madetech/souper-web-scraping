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
    # Insert report
    report_table = Report.__table__
    statement = insert(report_table).values(
        assessment_date=report.assessment_date,
        overall_verdict=report.overall_verdict,
        name=report.name,
        url=report.url,
        stage=report.stage
    )
    # Update report if conflicted with unique constraint
    statement = statement.on_conflict_do_update(
        constraint="report_url_key",
        set_=dict(
            overall_verdict=report.overall_verdict,
            stage=report.stage,
            assessment_date=report.assessment_date
        )
    )
    # Return the id of affected rows
    statement = statement.returning(report_table.c["id"])

    # Execute statement and extract report_id from result
    for row in conn.execute(statement):
        report_id = row[0]
        
    # Create list of section values with report_id
    sections = []
    for section in report.sections:
        sections.append(dict(
            report_id=report_id,
            number=section.number,
            decision=section.decision
        ))

    # Bulk insert sections
    statement = insert(Section.__table__).values(sections)

    # Update section if conflicted with unique constraint
    statement = statement.on_conflict_do_update(
        constraint="section_report_id_number_key",
        set_=dict(
            decision=statement.excluded.decision
        )
    )
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