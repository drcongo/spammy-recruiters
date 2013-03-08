"""add spammer frequency column

Revision ID: 4cd0c6a2736f
Revises: 358b3f6ca619
Create Date: 2012-12-20 17:26:40.632679

"""

# revision identifiers, used by Alembic.
revision = '4cd0c6a2736f'
down_revision = '358b3f6ca619'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column("address",
        sa.Column(
            "count",
            sa.Integer,
            default=1))


def downgrade():
    op.drop_column("address", "count")
