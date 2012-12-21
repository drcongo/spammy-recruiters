from webapp import app, db
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import func
from sqlalchemy.orm import validates

# auto-generated index names use the ix_table_column naming convention

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
    address = db.Column(
        db.String(250),
        nullable=False,
        unique=True,
        index=True)
    timestamp = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=func.now())
    count = db.Column(
        db.Integer(),
        default=1)

    def __init__(self, address):
        self.address = address

    @classmethod
    def exists(self, address):
        """ Check if an address exists, increment counter if it does """
        exsts = self.query.filter_by(address=address).first()
        if exsts:
            exsts.count += 1
            db.session.add(exsts)
            db.session.commit()
            return True
        return False

    @classmethod
    def top_three(self):
        """ Return top three most added spammers """
        return [{each.address: each.count} for each in 
            self.query.order_by(self.count.desc()).limit(3).all()]


class Counter(db.Model, SpamsubMixin):
    """
    Counter table
    """
    count = db.Column(
        db.Integer(),
        nullable=False,
        unique=True,
        index=True)
    timestamp = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=func.now())

    def __init__(self, count):
        self.count = count

    @validates('count')
    def validate_count(self, key, count):
        try:
            assert count >= 0
        except AssertionError:
            count = 0
        return count


class UpdateCheck(db.Model, SpamsubMixin):
    """ Update check timestamp """
    timestamp = db.Column(
        db.TIMESTAMP,
        nullable=False,
        default=func.now())

    def __init__(self):
        self.timestamp = func.now()
