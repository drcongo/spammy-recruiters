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


reg = re.compile(r"^[\w\-.]*\.[a-z]{2,4}$")


class SpammerForm(Form):
    error_msg = u""" The address you entered is wrong. Please type the recruiter's 
address as follows: Everything <em>after</em> the "@" sign, with no spaces.
<br>For example: <strong>enterprise-weasels.co.uk</strong> """
    address = StringField(u"Address Entry",[
        validators.DataRequired(
            message=u"You must enter an address."),
        validators.Regexp(
            reg,
            flags=0,
            message=error_msg)
    ])
    submit = SubmitField()
