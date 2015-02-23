from flask_wtf import (
    Form,
    RecaptchaField
    )
from wtforms import (
    StringField,
    SubmitField,
    validators
    )
import re


reg = re.compile(r"^[\w\-.]*\.[a-z]{2,4}$")


class SpammerForm(Form):
    error_msg = u"""The address you tried to add is wrong. Please type it
 like this:<ul><li>Everything <em>after</em> the "@" sign, with no spaces.</li>
<li>Example: <strong>enterprise-weasels.co.uk</strong></li></ul>"""
    address = StringField(
        u"Address Entry",
        [validators.DataRequired(
            message=u"You have to enter an address."),
            validators.Regexp(
                reg,
                flags=0,
                message=error_msg)]
    )
    recaptcha = RecaptchaField(
        label=u"ReCaptcha",
    )

    submit = SubmitField()
