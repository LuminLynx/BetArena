"""Seed database with sample data."""

from datetime import datetime, timedelta

from app.core.db import SessionLocal
from app.models.event import Event, EventStatus
from app.models.league import League
from app.models.team import Team


def seed_data():
    """Seed database with sample leagues, teams, and events."""
    db = SessionLocal()
    try:
        print("Starting database seeding...")

        # Check if data already exists
        existing_leagues = db.query(League).count()
        if existing_leagues > 0:
            print(f"Database already has {existing_leagues} leagues. Skipping seed.")
            return

        # Create Leagues
        print("Creating leagues...")
        epl = League(id=1, name="Premier League", country="England")
        primeira = League(id=2, name="Primeira Liga", country="Portugal")
        db.add_all([epl, primeira])
        db.flush()

        # Create Teams
        print("Creating teams...")
        # Premier League teams
        man_city = Team(
            id=1, league_id=epl.id, name="Manchester City", slug="manchester-city"
        )
        liverpool = Team(id=2, league_id=epl.id, name="Liverpool", slug="liverpool")

        # Primeira Liga teams
        benfica = Team(id=3, league_id=primeira.id, name="Benfica", slug="benfica")
        porto = Team(id=4, league_id=primeira.id, name="Porto", slug="porto")

        db.add_all([man_city, liverpool, benfica, porto])
        db.flush()

        # Create Events scheduled this week
        print("Creating events...")
        now = datetime.utcnow()

        # Event 1: Manchester City vs Liverpool (3 days from now)
        event1 = Event(
            id=1,
            league_id=epl.id,
            home_id=man_city.id,
            away_id=liverpool.id,
            start_time=now + timedelta(days=3),
            status=EventStatus.SCHEDULED,
        )

        # Event 2: Benfica vs Porto (5 days from now)
        event2 = Event(
            id=2,
            league_id=primeira.id,
            home_id=benfica.id,
            away_id=porto.id,
            start_time=now + timedelta(days=5),
            status=EventStatus.SCHEDULED,
        )

        db.add_all([event1, event2])
        db.commit()

        print("✅ Database seeded successfully!")
        print(f"  - Created {db.query(League).count()} leagues")
        print(f"  - Created {db.query(Team).count()} teams")
        print(f"  - Created {db.query(Event).count()} events")

    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
