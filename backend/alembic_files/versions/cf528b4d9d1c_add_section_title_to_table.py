"""add section title to table

Revision ID: cf528b4d9d1c
Revises: a2b4b15fd4ff
Create Date: 2023-07-31 12:14:18.730734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf528b4d9d1c'
down_revision = 'a2b4b15fd4ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('section', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('section', 'title')
    # ### end Alembic commands ###
