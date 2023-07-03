import time

from flask import Blueprint, request, redirect, url_for, render_template

from controller.authentication import is_authenticated
import view.event as view
from modal.event import Event

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('/')
def layout():
    time.sleep(1)
    if is_authenticated():
        result = view.find_all()
        events = result['event']
        departments = result['department']
        if events is None:
            return render_template('culturalhouse/event/layout.html', len=0, events=events)
        return render_template('culturalhouse/event/layout.html', len=len(events), events=events,
                               departments=departments)
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/edit/<id>')
def edit(id):
    time.sleep(1)

    if is_authenticated():
        event = view.find_by_id(id)
        return render_template('culturalhouse/event/edit.html', event=event)
    else:
        return redirect(url_for('authentication.login'))

@event_bp.route('/add/<id>')
def add(id):
    time.sleep(1)

    if is_authenticated():  
        if request.method == "POST":
            new_id = request.form.get('assetId')
            new_name = request.form.get('assetName')
            new_qty = request.form.get('assetQty')

            new_asset = Event(name = new_name, qty = new_qty)
            view.create(new_asset)
            return redirect(url_for('asset.detail', id = new_id))

        return render_template('culturalhouse/asset/add.html', assetId = view.generate_id())
    else:
        return render_template(url_for('authentication.login'))
