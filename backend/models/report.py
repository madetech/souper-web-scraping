import enum
from typing import List

import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Report(Base):
    __tablename__ = "report"
    id :Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    assessment_date: Mapped[str] = mapped_column(nullable=True)
    overall_verdict: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str]
    url: Mapped[str] = mapped_column(unique=True)
    stage: Mapped[str] = mapped_column(nullable=True)
    sections: Mapped[List["Section"]] = relationship()

class ReportOut(BaseModel):
    id: int
    assessment_date:str
    overall_verdict: str
    name: str
    url:str
    stage: str

    class ConfigDict:
        from_attributes = True


class Section(Base):
    __tablename__ = "section"
    __table_args__ = (
        UniqueConstraint("report_id", "number", name="section_report_id_number_key"),
    )

    id: Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    report_id: Mapped[int] = Column(Integer, ForeignKey("report.id"))
    number: Mapped[int]= mapped_column(nullable=True)
    decision: Mapped[str] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(nullable= True)
    feedback: Mapped[List["Feedback"]] = relationship()

class FeedbackType(enum.Enum):
    POSITIVE='positive'
    CONSTRUCTIVE='constructive'

class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    section_id = Column(Integer, ForeignKey("section.id"))
    feedback: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[FeedbackType] = mapped_column(
        sqlalchemy.Enum(FeedbackType, native_enum=False)
    )
