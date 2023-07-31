from models.report import Base, Feedback, Report, Section
from sqlalchemy import Connection
from sqlalchemy.dialects.postgresql import insert
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
    for report_row in conn.execute(statement):
        report_id = report_row[0]
        
        # Create list of section values with report_id
        sections = []
        for section in report.sections:
            sections.append(dict(
                report_id=report_id,
                number=section.number,
                decision=section.decision,
                title = section.title
            ))

        # Bulk insert sections
        if any(sections):
            section_table = Section.__table__
            statement = insert(Section.__table__).values(sections)

            # Update section if conflicted with unique constraint
            statement = statement.on_conflict_do_update(
                constraint="section_report_id_number_key",
                set_=dict(
                    decision=statement.excluded.decision
                )
            )

            statement = statement.returning(section_table.c["id"])

            for section_row in conn.execute(statement):
                section_id = section_row[0]
            
                feedback = []
                for feedback_line in section.feedback:
                    feedback.append(dict(
                        section_id = section_id,
                        feedback = feedback_line.feedback,
                        type = feedback_line.type
                    ))

                if any(feedback):
                    statement = insert(Feedback.__table__).values(feedback)

    conn.commit()
    conn.close()