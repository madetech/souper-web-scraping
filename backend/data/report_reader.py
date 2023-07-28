from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Report, ReportOut
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session


def get_reports(engine: Engine) -> LimitOffsetPage[ReportOut]:
        with Session(engine) as database, database.begin():
            return paginate(database, select(Report))
