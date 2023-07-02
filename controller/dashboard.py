from flask import Blueprint, render_template, redirect, url_for

from controller.authentication import is_authenticated
from view.general import Information

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def layout():
    if is_authenticated():
        information = Information()
        return render_template('dashboard/layout.html', information=information)
    else:
        return redirect(url_for('authentication.login'))
