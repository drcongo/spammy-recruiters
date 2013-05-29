from sqlalchemy.orm import validates
from apps.shared.models import db, AppMixin

# auto-generated index names use the ix_table_column naming convention


class Address(db.Model, AppMixin):
    """ Address table """
    address = db.Column(
        db.String(250),
        nullable=False,
        unique=True,
        index=True)
    count = db.Column(
        db.Integer(),
        default=1)
    pending = db.Column(
        db.Boolean(),
        default=True)
    sent = db.Column(
        db.Boolean(),
        default=False)
    complete = db.Column(
        db.Boolean(),
        default=False)

    def __init__(self, address, pending, sent, complete):
        self.address = address
        self.pending = pending
        self.sent = sent
        self.complete = complete

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
    def top(self, number=3):
        """ Return top spammers """
        return [{"x": each.address, "y": each.count} for each in
                self.query.order_by(self.count.desc()).limit(number).all()]


class Counter(db.Model, AppMixin):
    """ Counter table """
    count = db.Column(
        db.Integer(),
        nullable=False,
        unique=True,
        index=True)

    def __init__(self, count):
        self.count = count

    @validates('count')
    def validate_count(self, key, count):
        try:
            assert count >= 0
        except AssertionError:
            count = 0
        return count


class UpdateCheck(db.Model, AppMixin):
    """ Update check timestamp table """

    def __init__(self):
        pass
