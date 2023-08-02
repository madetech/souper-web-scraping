from models.report import Feedback, Report, Section
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session


def upsert_report(reports: list[Report], session: Session):
   report_table = Report.__table__
   section_table = Section.__table__
   feedback_table = Feedback.__table__
   
   for report in reports:

      # Insert report
      upsert_report_statement = insert(report_table).values(
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
      
      row = session.execute(upsert_report_statement).fetchone()
      report_id = row[0]

      for section in report.sections:
         section_to_insert = dict(
               report_id=report_id,
               number=section.number,
               title=section.title,
               decision=section.decision
         )

         upsert_section_statement = insert(section_table).values(section_to_insert)
         upsert_section_statement = upsert_section_statement.on_conflict_do_update(
                                       constraint="section_report_id_number_key",
                                       set_=dict(
                                          decision=upsert_section_statement.excluded.decision,
                                          title=upsert_section_statement.excluded.title,
                                       )
                                    ).returning(section_table.c["id"])
      
         inserted_section = session.execute(upsert_section_statement).fetchone()

         section_id = inserted_section[0]
      
         feedbacks_to_insert = []
         for feedback_item in section.feedback:
            feedbacks_to_insert.append(dict(
                  section_id = section_id,
                  feedback = feedback_item.feedback,
                  type = feedback_item.type
            ))

         if any(feedbacks_to_insert):
            session.execute(insert(feedback_table).values(feedbacks_to_insert))

   session.commit()