from typing import List

from models.section import Feedback
from sqlalchemy.orm import Session


def get_feedback(id, session: Session) -> List[Feedback]:
    with session:
        return session.query(Feedback).filter(Feedback.section_id == id).all()