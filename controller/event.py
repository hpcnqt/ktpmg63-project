import time

from flask import Blueprint, request, redirect, url_for, render_template

from controller.authentication import is_authenticated
from modal.event import Event
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
        return render_template('culturalhouse/event/layout.html', len=len(events), events=events, departments=departments)
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    time.sleep(1)

    if is_authenticated():
        event = view.find_by_id(id)
        departments = view.find_all_departments()

        if request.method == 'POST':
            eventName = request.form.get('eventName')
            registerName = request.form.get('registerName')
            registerContact = request.form.get('registerContact')
            department = request.form.get('department')
            fee = request.form.get('fee')
            fromTime = request.form.get('fromTime')
            toTime = request.form.get('toTime')
            status = event.status

            updated_event = Event(name=eventName, owner=registerName, fee=fee,
                                  contact=registerContact, department_id=int(department),
                                  from_time=fromTime, to_time=toTime, status=status)

            updated_event.id=id

            view.update(updated_event)
            return redirect(url_for('event.detail', id=event.id))

        return render_template('culturalhouse/event/edit.html', event=event, departments=departments, len=len(departments))
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/detail/<id>')
def detail(id):
    time.sleep(1)

    if is_authenticated():
        event = view.find_by_id(id)
        return render_template('culturalhouse/event/detail.html', event=event)
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/accept/<id>')
def accept(id):
    time.sleep(1)

    if is_authenticated():
        event = view.find_by_id(id=id)
        view.update_status(event)

        return redirect(url_for('event.layout'))
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/add', methods=['GET', 'POST'])
def add():
    time.sleep(1)

    if is_authenticated():
        departments = view.find_all_departments()
        if request.method == 'POST':
            event_name = request.form.get('eventName')
            owner = request.form.get('registerName')
            owner_contact = request.form.get('registerContact')
            department_id = request.form.get('department')
            fee = request.form.get('fee')
            from_time = request.form.get('fromTime')
            to_time = request.form.get('toTime')
            status = 0

            event = Event(event_name, owner, owner_contact, fee, status, from_time, to_time, department_id)
            view.create(event)
            return redirect(url_for('event.layout'))
        return render_template('culturalhouse/event/add.html', len=len(departments), departments=departments)
    else:
        return redirect(url_for('authentication.login'))


@event_bp.route('/remove/<id>', methods=['POST'])
def remove(id):
    time.sleep(1)

    if is_authenticated():
        if request.method == 'POST':
            event = view.find_by_id(id)
            view.remove(event)
            return redirect(url_for('event.layout'))
    else:
        return redirect(url_for('authentication.login'))