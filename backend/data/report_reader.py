from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Report
from sqlalchemy import select


def get_reports(database):
    return paginate(database, select(Report))
        