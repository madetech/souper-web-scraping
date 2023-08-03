from typing import List

from models.section import Section
from sqlalchemy.orm import Session


def get_sections(id, session: Session) -> List[Section]:
   with session:
      return session.query(Section).filter(Section.report_id == id).all()
