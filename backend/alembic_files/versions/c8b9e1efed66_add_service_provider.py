"""add service_provider

Revision ID: c8b9e1efed66
Revises: b5bfc01c69e5
Create Date: 2023-08-11 12:10:22.406131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8b9e1efed66'
down_revision = 'b5bfc01c69e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('report', sa.Column('service_provider', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('report', 'service_provider')
