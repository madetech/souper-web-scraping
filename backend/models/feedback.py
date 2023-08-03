import enum

import sqlalchemy
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column


class FeedbackType(enum.Enum):
    POSITIVE='positive'
    CONSTRUCTIVE='constructive'


class Feedback(Base):
    __tablename__ = "feedback"
    __table_args__ = (
        UniqueConstraint("section_id", "feedback", "type", name="feedback_section_id_feedback_type_key"),
    )

    id: Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    section_id = Column(Integer, ForeignKey("section.id"))
    feedback: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[FeedbackType] = mapped_column(
        sqlalchemy.Enum(FeedbackType, native_enum=False)
    )