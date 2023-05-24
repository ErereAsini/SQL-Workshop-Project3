"""create customers

Revision ID: 098801024a99
Revises: 
Create Date: 2023-04-25 18:44:07.133831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '098801024a99'
down_revision = None
branch_labels = None
depends_on = None

# pylint: disable=E1101

def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
