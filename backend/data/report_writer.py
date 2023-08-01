from models.report import Report
from sqlalchemy.orm import Session


def upsert_report(reports: list[Report], session: Session):
   session.add_all(reports)
   session.commit()