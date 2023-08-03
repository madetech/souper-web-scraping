from typing import List

from models.section import Section
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


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



