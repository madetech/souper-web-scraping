import enum

import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


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