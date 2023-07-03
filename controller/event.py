import time

from flask import Blueprint, request, redirect, url_for, render_template

from controller.authentication import is_authenticated
import view.event as view

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
        departments = view.find_all_departments()
        return render_template('culturalhouse/event/edit.html', event=event, departments=departments, len=len(departments))
    else:
        return redirect(url_for('authentication.login'))
