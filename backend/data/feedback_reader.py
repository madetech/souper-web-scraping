from typing import List

from models.section import Feedback
from sqlalchemy.orm import Session


def get_feedback(id, session: Session) -> List[Feedback]:
    with session:
        #return id
        return session.query(Feedback).filter(Feedback.section_id == id).all()
        #return session.query(Feedback).all()


# def get_feedback(id, session: Session) -> List[Feedback]:
#     with session:
#         query = session.query(Feedback)
#         return filter_feedback(query, id)
    

# def filter_feedback(query, id) -> List[Feedback]:
#     return query.filter_by(Feedback.section_id == id).all()