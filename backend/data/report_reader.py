
from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Report, ReportOut
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_reports(session: Session) -> list[ReportOut]:
        with session:
                return session.query(ReportOut).all()
             

