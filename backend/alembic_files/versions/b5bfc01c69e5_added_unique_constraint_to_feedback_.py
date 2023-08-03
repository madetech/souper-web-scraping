"""added unique constraint to feedback table to prevent duplicates

Revision ID: b5bfc01c69e5
Revises: e1430be9db45
Create Date: 2023-08-03 11:43:14.140741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5bfc01c69e5'
down_revision = 'e1430be9db45'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('feedback_section_id_feedback_type_key', 'feedback', ['section_id', 'feedback', 'type'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('feedback_section_id_feedback_type_key', 'feedback', type_='unique')
    # ### end Alembic commands ###
