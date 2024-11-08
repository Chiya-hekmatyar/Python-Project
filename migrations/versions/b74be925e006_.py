"""empty message

Revision ID: b74be925e006
Revises: f62ae8cf1d01
Create Date: 2024-10-30 14:06:46.390638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b74be925e006'
down_revision = 'f62ae8cf1d01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('member_since', sa.DateTime(), nullable=True, server_default=sa.func.now()))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('img', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True,server_default='1'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('active')
        batch_op.drop_column('img')
        batch_op.drop_column('last_seen')
        batch_op.drop_column('member_since')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
