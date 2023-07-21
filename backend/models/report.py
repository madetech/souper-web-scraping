from typing import Any

from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Report(Base):
    __tablename__ = "report"
    id :Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    assessment_date: Mapped[str | None] = mapped_column(nullable=True)
    overall_verdict: Mapped[str | None] = mapped_column(nullable=True)
    name: Mapped[str]
    url: Mapped[str] = mapped_column(unique=True)
    stage: Mapped[str | None] = mapped_column(nullable=True)
    # sections: relationship("Section")

class ReportOut(BaseModel):
    id: int
    assessment_date:str
    overall_verdict: str
    name: str
    url:str
    stage: str

    class Config:
        orm_mode = True

class Section(Base):
    __tablename__ = "section"
    id :Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    section_id: Any = Column(Integer, ForeignKey("report.id"))
    number: Mapped[int]
    decision: Mapped[str] # default null
    feedback: Mapped[str]