# this is a shared db instance for blueprints
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import validates
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class utcnow(expression.FunctionElement):
    """ UTC Timestamp for compilation """
    type = DateTime()


# Define PG utcnow() function
@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    """ Postgres UTC Timestamp """
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class AppMixin(object):
    """ Provides some common attributes to our models """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __mapper_args__ = {'always_refresh': True}

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(DateTime, nullable=False, server_default=utcnow())
