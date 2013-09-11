import os
from flask import (
    Blueprint,
    request,
    flash,
    render_template,
    send_file,
    jsonify,
    current_app
)
from models import *
from forms import SpammerForm
import utils

spamsub = Blueprint(
    'spamsub',
    __name__,
    template_folder='templates'
)


@spamsub.route('/', methods=['GET', 'POST'])
def index():
    """ Index page """
    count = Address.query.count()
    form = SpammerForm()
    # try to validate, and check for AJAX submission
    if form.validate_on_submit():
        if not utils.check_if_exists(form.address.data):
            flash(
                u"We've added %s to the database." % form.address.data,
                "text-success")
        else:
            flash(
                u"We already know about %s, though." % form.address.data,
                "text-success")
    if request.is_xhr:
        # OK to send back a fragment
        return render_template(
            'form.jinja',
            form=form,
        )
    # GET or no JS, so render a full page
    return render_template(
        'index.jinja',
        form=form,
        count=count,
        recaptcha_public_key=current_app.config['RECAPTCHA_PUBLIC_KEY'])


@spamsub.route('download', methods=['GET'])
def download():
    """ Download the latest version of spammers.txt """
    utils.update_db()
    return send_file(
        os.path.join(utils.basename, "git_dir/spammers.txt"),
        as_attachment=True,
        attachment_filename="spammers.txt")


@spamsub.route('updates', methods=['GET'])
def updates():
    """ Check for updates in GitHub repo if more than an hour's passed """
    vals = {
        'last_updated': utils.sync_check(),
        'count': Address.query.count(),
    }
    return jsonify(vals)
