"""update models schema

Revision ID: a7742f611f01
Revises: 9720ec0dedab
Create Date: 2020-11-13 18:46:16.777838

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "a7742f611f01"
down_revision = "9720ec0dedab"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Show",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("artist_id", sa.Integer(), nullable=False),
        sa.Column("venue_id", sa.Integer(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["artist_id"],
            ["Artist.id"],
        ),
        sa.ForeignKeyConstraint(
            ["venue_id"],
            ["Venue.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("Shows")
    op.add_column(
        "Artist", sa.Column("seeking_description", sa.String(length=120), nullable=True)
    )
    op.add_column(
        "Artist", sa.Column("seeking_venue", sa.String(length=120), nullable=True)
    )
    op.add_column("Artist", sa.Column("website", sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("Artist", "website")
    op.drop_column("Artist", "seeking_venue")
    op.drop_column("Artist", "seeking_description")
    op.create_table(
        "Shows",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('\"Shows_id_seq\"'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("artist_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("venue_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            "start_time", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["artist_id"], ["Artist.id"], name="Shows_artist_id_fkey"
        ),
        sa.ForeignKeyConstraint(["venue_id"], ["Venue.id"], name="Shows_venue_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="Shows_pkey"),
    )
    op.drop_table("Show")
    # ### end Alembic commands ###
