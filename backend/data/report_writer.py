from models.feedback import Feedback
from models.report import Report
from models.section import Section
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

REPORT_TABLE = Report.__table__
SECTION_TABLE = Section.__table__
FEEDBACK_TABLE = Feedback.__table__

def upsert_reports(reports: list[Report], session: Session):
   
   for report in reports:

      report_id = upsert_report(report, session)

      for section in report.sections:
        section_id = upsert_report_section(section, report_id, session)
        
        bulk_upsert_feedback(section, section_id, session)

   session.commit()

def upsert_report(report: Report, session: Session):
   # Insert report
      upsert_report_statement = insert(REPORT_TABLE).values(
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
         ).returning(REPORT_TABLE.c["id"])
      
      row = session.execute(upsert_report_statement).fetchone()
      return row[0] # report id

def upsert_report_section(section: Section, report_id: int, session: Session):
    section_to_insert = dict(
               report_id=report_id,
               number=section.number,
               title=section.title,
               decision=section.decision
        )

    upsert_section_statement = insert(SECTION_TABLE).values(section_to_insert)
    upsert_section_statement = upsert_section_statement.on_conflict_do_update(
                                constraint="section_report_id_number_key",
                                set_=dict(
                                    decision=upsert_section_statement.excluded.decision,
                                    title=upsert_section_statement.excluded.title,
                                )
                            ).returning(SECTION_TABLE.c["id"])

    inserted_section = session.execute(upsert_section_statement).fetchone()

    return inserted_section[0] # section id

def bulk_upsert_feedback(section: Section, section_id: int, session: Session):
    feedbacks_to_insert = []

    for feedback_item in section.feedback:
        feedbacks_to_insert.append(dict(
                section_id = section_id,
                feedback = feedback_item.feedback,
                type = feedback_item.type
        ))

    if any(feedbacks_to_insert):
      session.execute(insert(FEEDBACK_TABLE).values(feedbacks_to_insert))