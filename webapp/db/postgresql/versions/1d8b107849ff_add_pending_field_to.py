"""Add 'pending' field to Address

Revision ID: 1d8b107849ff
Revises: 31d14d064445
Create Date: 2013-05-28 23:55:29.810952

"""

# revision identifiers, used by Alembic.
revision = '1d8b107849ff'
down_revision = '31d14d064445'

from alembic import op
import sqlalchemy as sa


def upgrade():
        op.add_column(
            "address",
            sa.Column(
                "pending",
                sa.Boolean,
                default=True))


def downgrade():
    op.drop_column("address", "pending")
