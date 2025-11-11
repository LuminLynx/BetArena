"""Event model."""

import enum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer

from app.models.base import Base


class EventStatus(str, enum.Enum):
    """Event status enumeration."""

    SCHEDULED = "scheduled"
    LIVE = "live"
    FINISHED = "finished"


class Event(Base):
    """Event/Match model."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False, index=True)
    home_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)
    away_id = Column(Integer, ForeignKey("teams.id"), nullable=False, index=True)
    start_time = Column(DateTime, nullable=False, index=True)
    status = Column(
        Enum(EventStatus, native_enum=False, length=20),
        nullable=False,
        default=EventStatus.SCHEDULED,
        index=True,
    )

    def __repr__(self):
        return (
            f"<Event(id={self.id}, home_id={self.home_id}, "
            f"away_id={self.away_id}, status='{self.status}')>"
        )
