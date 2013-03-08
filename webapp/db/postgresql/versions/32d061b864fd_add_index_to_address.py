"""Add index to address field

Revision ID: 32d061b864fd
Revises: 622a69a8204
Create Date: 2012-10-05 17:39:19.912912

"""

# revision identifiers, used by Alembic.
revision = '32d061b864fd'
down_revision = '622a69a8204'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_index(
        "address_idx", "address", ['address'])


def downgrade():
    op.drop_index("address_idx", "address")
