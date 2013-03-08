"""Alter timestamp columns

Revision ID: 31d14d064445
Revises: 4cd0c6a2736f
Create Date: 2012-12-24 11:55:39.306586

"""

# revision identifiers, used by Alembic.
revision = '31d14d064445'
down_revision = '4cd0c6a2736f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime



# define a "UTC" timestamp class
class utcnow(expression.FunctionElement):
    """ UTC Timestamp """
    type = DateTime()


# Define PG and MYSQL utcnow() functions
@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    """ Postgres UTC Timestamp """
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(utcnow, 'mssql')
def ms_utcnow(element, compiler, **kw):
    """ MySQL UTC Timestamp """
    return "GETUTCDATE()"


def upgrade():
    op.alter_column("address", "timestamp", type_=DateTime,
        server_default=utcnow())
    op.alter_column("updatecheck", "timestamp", type_=DateTime,
        server_default=utcnow())
    op.alter_column("counter", "timestamp", type_=DateTime,
        server_default=utcnow())


def downgrade():
    op.alter_column("address", "timestamp",
        type_=sa.TIMESTAMP, server_default=sa.func.now())
    op.alter_column("updatecheck", "timestamp", type_=sa.TIMESTAMP,
        server_default=sa.func.now())
    op.alter_column("counter", "timestamp", type_=sa.TIMESTAMP,
        server_default=sa.func.now())
