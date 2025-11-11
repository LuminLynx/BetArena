"""League model."""

from sqlalchemy import Column, Integer, String

from app.models.base import Base


class League(Base):
    """League/Competition model."""

    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<League(id={self.id}, name='{self.name}', country='{self.country}')>"
