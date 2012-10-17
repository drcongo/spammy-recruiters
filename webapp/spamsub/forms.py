from flask.ext.wtf import (
    Form,
    Required,
    TextAreaField,
    StringField,
    RadioField,
    HiddenField,
    SubmitField,
    validators
    )
import re

reg = re.compile(r"^@[\w\-.]*\.[a-z]{2,4}$")


class SpammerForm(Form):
    address = StringField(u"Address Entry",[
        validators.DataRequired(
            message=u"You must enter an address."),
        validators.Regexp(
            reg,
            flags=0,
            message=u"Invalid address. The address must begin with an '@'.")
    ])
    submit = SubmitField()
