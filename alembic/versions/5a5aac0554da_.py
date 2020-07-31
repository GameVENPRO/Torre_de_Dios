"""empty message

Revision ID: 5a5aac0554da
Revises: 7185e7032909
Create Date: 2020-07-30 19:46:52.077641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a5aac0554da'
down_revision = '7185e7032909'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False, comment='Уникальный ид операции'),
    sa.Column('item_id', sa.Integer(), nullable=False, comment='Ид продаваемого предмета'),
    sa.Column('item', sa.String(), nullable=False, comment='Продаваемый предмет'),
    sa.Column('rank', sa.String(length=1), nullable=False, comment='Ранг'),
    sa.Column('price', sa.Integer(), nullable=False, comment='Цена предмета'),
    sa.Column('user_id', sa.Integer(), nullable=False, comment='ИД продавца'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop')
    # ### end Alembic commands ###