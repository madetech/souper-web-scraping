from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Report, ReportOut
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_reports(session: Session) -> LimitOffsetPage[ReportOut]:
        with session:
            return paginate(session, select(Report))
