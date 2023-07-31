from typing import List

from models.report import Section
from sqlalchemy import Engine
from sqlalchemy.orm import Session


def get_sections(id, engine: Engine) -> List[Section]:
   with Session(engine) as session:
      return session.query(Section).filter(Section.report_id == id).all()