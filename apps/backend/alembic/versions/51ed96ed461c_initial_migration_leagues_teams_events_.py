"""Initial migration: leagues, teams, events, results

Revision ID: 51ed96ed461c
Revises:
Create Date: 2025-11-11 17:30:49.782970

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "51ed96ed461c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create leagues table
    op.create_table(
        "leagues",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("country", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_leagues_id"), "leagues", ["id"], unique=False)

    # Create teams table
    op.create_table(
        "teams",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("league_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.ForeignKeyConstraint(
            ["league_id"],
            ["leagues.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index(op.f("ix_teams_id"), "teams", ["id"], unique=False)
    op.create_index(op.f("ix_teams_league_id"), "teams", ["league_id"], unique=False)
    op.create_index(op.f("ix_teams_slug"), "teams", ["slug"], unique=True)

    # Create events table
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("league_id", sa.Integer(), nullable=False),
        sa.Column("home_id", sa.Integer(), nullable=False),
        sa.Column("away_id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "scheduled",
                "live",
                "finished",
                name="eventstatus",
                native_enum=False,
                length=20,
            ),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["away_id"],
            ["teams.id"],
        ),
        sa.ForeignKeyConstraint(
            ["home_id"],
            ["teams.id"],
        ),
        sa.ForeignKeyConstraint(
            ["league_id"],
            ["leagues.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_events_away_id"), "events", ["away_id"], unique=False)
    op.create_index(op.f("ix_events_home_id"), "events", ["home_id"], unique=False)
    op.create_index(op.f("ix_events_id"), "events", ["id"], unique=False)
    op.create_index(op.f("ix_events_league_id"), "events", ["league_id"], unique=False)
    op.create_index(
        op.f("ix_events_start_time"), "events", ["start_time"], unique=False
    )
    op.create_index(op.f("ix_events_status"), "events", ["status"], unique=False)

    # Create results table
    op.create_table(
        "results",
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("home_goals", sa.Integer(), nullable=False),
        sa.Column("away_goals", sa.Integer(), nullable=False),
        sa.Column("settled_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.PrimaryKeyConstraint("event_id"),
    )


def downgrade() -> None:
    # Drop tables in reverse order
    op.drop_table("results")
    op.drop_index(op.f("ix_events_status"), table_name="events")
    op.drop_index(op.f("ix_events_start_time"), table_name="events")
    op.drop_index(op.f("ix_events_league_id"), table_name="events")
    op.drop_index(op.f("ix_events_id"), table_name="events")
    op.drop_index(op.f("ix_events_home_id"), table_name="events")
    op.drop_index(op.f("ix_events_away_id"), table_name="events")
    op.drop_table("events")
    op.drop_index(op.f("ix_teams_slug"), table_name="teams")
    op.drop_index(op.f("ix_teams_league_id"), table_name="teams")
    op.drop_index(op.f("ix_teams_id"), table_name="teams")
    op.drop_table("teams")
    op.drop_index(op.f("ix_leagues_id"), table_name="leagues")
    op.drop_table("leagues")
    # Drop enum type if it exists
    sa.Enum(name="eventstatus").drop(op.get_bind(), checkfirst=True)
