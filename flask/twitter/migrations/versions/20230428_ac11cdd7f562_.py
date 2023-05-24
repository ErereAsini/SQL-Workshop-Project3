"""empty message

Revision ID: ac11cdd7f562
Revises: 
Create Date: 2023-04-28 11:03:09.329764

"""
from alembic import op
import sqlalchemy as sa

# pylint: disable=E1101

# revision identifiers, used by Alembic.
revision = 'ac11cdd7f562'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###