"""Team model."""

from sqlalchemy import Column, ForeignKey, Integer, String

from app.models.base import Base


class Team(Base):
    """Team model."""

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True, index=True)

    def __repr__(self):
        return f"<Team(id={self.id}, name='{self.name}', slug='{self.slug}')>"
