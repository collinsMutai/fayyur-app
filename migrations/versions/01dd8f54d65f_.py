"""empty message

Revision ID: 01dd8f54d65f
Revises: 101e2a704460
Create Date: 2020-11-08 05:52:46.589673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01dd8f54d65f'
down_revision = '101e2a704460'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'deleted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('deleted', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
