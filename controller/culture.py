import time

from flask import Blueprint, render_template, redirect, url_for, request
from controller.authentication import is_authenticated


culture_bp = Blueprint('culture', __name__)

@culture_bp.route('/culture/event')
def event():
    if is_authenticated():
        return render_template('culture/event.html')
    else:
        return redirect(url_for('authentication.login'))
    
@culture_bp.route('/culture/device')
def device():
    if is_authenticated():
        return render_template('culture/device.html')
    else:
        return redirect(url_for('authentication.login'))

