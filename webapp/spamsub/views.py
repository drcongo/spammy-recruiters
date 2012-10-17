from spamsub import app, db
from flask import request, flash, render_template, make_response, send_file
from models import *
from forms import SpammerForm
import utils


@app.route('/', methods=['GET', 'POST'])
def index():
    """ Index page """
    count = Address.query.count()
    form = SpammerForm()
    if request.method == 'POST' and request.is_xhr:
        # put request vars into a form and try to validate
        form.address = request.form.get('address')
        form.csrf_token = request.form.get('csrf_token')
        new_form = SpammerForm()
        if form.validate_on_submit():
            if not utils.check_if_exists(form.address):
                # process the address
                # send back thank you, and a new form
                flash(u"Thanks!", "text-success")
            else:
                # address exists, send back an error and a new form
                flash(u"We already know that spammer!", "text-error")
        else:
            # Validation error
            new_form._errors = form.errors
        return render_template('form.jinja', form=new_form)
    # GET, just render a page with a blank form
    return render_template('index.jinja', form=form, count=count)

@app.route('/download', methods=['GET'])
def download():
    """ Download the latest version of spammers.txt """
    utils.update_db()
    return send_file(
        "git_dir/spammers.txt",
        as_attachment=True,
        attachment_filename="spammers.txt")
