
from models.report import Report, ReportOut
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_reports(session: Session) -> list[Report]:
        with session:
                return session.query(Report).order_by(Report.assessment_date.desc()).all()
             
# filtering the reports by date removes the need for the buttons on page which affect pagination
