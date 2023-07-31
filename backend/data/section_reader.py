from typing import List
from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from models.report import Section 
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_sections(id, database: Session) -> List[Section]:

   return database.query(Section).filter(Section.report_id == id).all()


