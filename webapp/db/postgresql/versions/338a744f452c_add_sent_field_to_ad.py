"""Add 'sent' field to Address

Revision ID: 338a744f452c
Revises: 1d8b107849ff
Create Date: 2013-05-29 11:40:12.068834

"""

# revision identifiers, used by Alembic.
revision = '338a744f452c'
down_revision = '1d8b107849ff'

from alembic import op
import sqlalchemy as sa


def upgrade():
        op.add_column(
            "address",
            sa.Column(
                "sent",
                sa.Boolean,
                default=False))


def downgrade():
    op.drop_column("address", "sent")
