"""adding an update check table

Revision ID: 3afd1b623cca
Revises: 2f6bf42fb428
Create Date: 2012-11-10 01:28:45.605044

"""

# revision identifiers, used by Alembic.
revision = '3afd1b623cca'
down_revision = '2f6bf42fb428'

from alembic import op
import sqlalchemy as sa


def upgrade():
        updatecheck = op.create_table(
        "updatecheck",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column('timestamp', sa.TIMESTAMP, server_default=sa.func.now())
        )
        op.create_index(
        "update_timestamp", "updatecheck", ['timestamp'])



def downgrade():
    op.drop_table("updatecheck")
