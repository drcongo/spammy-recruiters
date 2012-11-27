"""Add indexes

Revision ID: 358b3f6ca619
Revises: 3afd1b623cca
Create Date: 2012-11-27 13:23:46.777375

"""

# revision identifiers, used by Alembic.
revision = '358b3f6ca619'
down_revision = '3afd1b623cca'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index(
        "ix_address_address", "address", ['address'])
    op.create_index(
        "ix_counter_count", "counter", ['count'])
    op.create_index(
        "ix_updatecheck_timestamp", "updatecheck", ['timestamp'])


def downgrade():
    op.drop_index("ix_address_address", "address")
    op.drop_index("ix_counter_count", "counter")
    op.drop_index("ix_updatecheck_timestamp", "updatecheck")
