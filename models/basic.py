from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text


class Base(DeclarativeBase):
    pass

class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    assessment_date: str # also reassessment
    overall_verdict: str
    name: str
    url: str
    # sections: relationship("Section")

class Section(Base):
    __tablename__ = "section"
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("report.id"))
    number: int
    decision: str # default null
    feedback: str