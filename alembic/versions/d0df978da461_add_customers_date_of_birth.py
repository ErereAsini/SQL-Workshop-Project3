"""add customers date_of_birth

Revision ID: d0df978da461
Revises: 098801024a99
Create Date: 2023-04-26 11:02:57.779312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0df978da461'
down_revision = '098801024a99'
branch_labels = None
depends_on = None

# pylint: disable=E1101

def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth TO dob;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN dob TO date_of_birth;
        """
    )
