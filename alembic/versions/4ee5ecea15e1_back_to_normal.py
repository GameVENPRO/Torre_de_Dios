"""back to normal

Revision ID: 4ee5ecea15e1
Revises: 63c48a55350f
Create Date: 2020-07-27 22:37:10.129983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ee5ecea15e1'
down_revision = '63c48a55350f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'healing')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('healing', sa.BOOLEAN(), autoincrement=False, nullable=True, comment='Лечение'))
    # ### end Alembic commands ###