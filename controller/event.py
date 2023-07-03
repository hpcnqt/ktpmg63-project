from flask import Blueprint

event_bp = Blueprint('event', __name__, url_prefix='/event')


@event_bp.route('/')
def layout():
    return "HeHe"
