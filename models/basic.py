from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text

from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    pass

class Report(Base):
    __tablename__ = "report"
    id :Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    assessment_date: Mapped[str] # also reassessment
    overall_verdict: Mapped[str]
    name: Mapped[str]
    url: Mapped[str]
    # sections: relationship("Section")

class Section(Base):
    __tablename__ = "section"
    id :Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    section_id = Column(Integer, ForeignKey("report.id"))
    number: Mapped[int]
    decision: Mapped[str] # default null
    feedback: Mapped[str]