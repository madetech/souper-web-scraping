
from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Report, ReportOut
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_reports(session: Session) -> list[Report]:
        with session:
                return session.query(Report).all()
             

