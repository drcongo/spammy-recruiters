from spamsub import db
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import func


class SpamsubMixin(object):
    """
    Provides some common attributes to our models
    """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __mapper_args__ = {'always_refresh': True}
    id = db.Column(db.Integer, primary_key=True)


class Address(db.Model, SpamsubMixin):
    """
    Address table
    """
    address = db.Column(db.String(250), nullable=False, unique=True)
    timestamp = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=func.now())

    def __init__(self, address):
        self.address = address


class Counter(db.Model, SpamsubMixin):
    """
    Counter table
    """
    count = db.Column(db.Integer(), nullable=False, unique=True)
    timestamp = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=func.now())

    def __init__(self, count):
        assert count >= 0
        self.count = count
