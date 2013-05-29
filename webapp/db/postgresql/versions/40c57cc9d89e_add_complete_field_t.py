"""Add 'complete' field to Address

Revision ID: 40c57cc9d89e
Revises: 338a744f452c
Create Date: 2013-05-29 13:57:25.047212

"""

# revision identifiers, used by Alembic.
revision = '40c57cc9d89e'
down_revision = '338a744f452c'

from alembic import op
import sqlalchemy as sa


def upgrade():
        op.add_column(
            "address",
            sa.Column(
                "complete",
                sa.Boolean,
                default=True))


def downgrade():
    op.drop_column("address", "complete")
