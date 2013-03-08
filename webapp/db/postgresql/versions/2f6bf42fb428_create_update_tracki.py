"""create update tracking table

Revision ID: 2f6bf42fb428
Revises: 32d061b864fd
Create Date: 2012-10-17 18:44:24.652632

"""

# revision identifiers, used by Alembic.
revision = '2f6bf42fb428'
down_revision = '32d061b864fd'

from alembic import op
import sqlalchemy as sa


def upgrade():
        counter = op.create_table(
        "counter",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("count", sa.Integer(), unique=True, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now())
        )
        op.create_index(
        "count_idx", "counter", ['count'])



def downgrade():
    op.drop_table("counter")
