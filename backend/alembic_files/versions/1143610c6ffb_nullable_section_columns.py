"""Nullable section columns

Revision ID: 1143610c6ffb
Revises: 61c05288192f
Create Date: 2023-07-20 16:51:29.995711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1143610c6ffb'
down_revision = '61c05288192f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('section', sa.Column('report_id', sa.Integer(), nullable=True))
    op.alter_column('section', 'number',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('section', 'decision',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('section', 'feedback',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint('section_section_id_fkey', 'section', type_='foreignkey')
    op.create_foreign_key(None, 'section', 'report', ['report_id'], ['id'])
    op.drop_column('section', 'section_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('section', sa.Column('section_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'section', type_='foreignkey')
    op.create_foreign_key('section_section_id_fkey', 'section', 'report', ['section_id'], ['id'])
    op.alter_column('section', 'feedback',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('section', 'decision',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('section', 'number',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('section', 'report_id')
    # ### end Alembic commands ###