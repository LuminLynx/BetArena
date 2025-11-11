"""Result model."""

from sqlalchemy import Column, DateTime, ForeignKey, Integer

from app.models.base import Base


class Result(Base):
    """Result model for finished events."""

    __tablename__ = "results"

    event_id = Column(
        Integer, ForeignKey("events.id"), primary_key=True, nullable=False
    )
    home_goals = Column(Integer, nullable=False)
    away_goals = Column(Integer, nullable=False)
    settled_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return (
            f"<Result(event_id={self.event_id}, home_goals={self.home_goals}, "
            f"away_goals={self.away_goals})>"
        )
