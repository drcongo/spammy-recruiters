"""Create address table

Revision ID: 622a69a8204
Revises: None
Create Date: 2012-10-03 11:49:27.071970

"""

# revision identifiers, used by Alembic.
revision = '622a69a8204'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
        address = op.create_table(
        "address",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("address", sa.String(250), unique=True, nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now())
        )



def downgrade():
    op.drop_table("address")
