import modal.event
import modal.event as modal_event
import modal.department as modal_department


def find_all_departments():
    return modal_department.find_all()


def find_all():
    result = dict()
    result['event'] = modal_event.find_all()
    result['department'] = modal_department.find_all()
    return result


def find_by_id(id):
    return modal_event.find_by_id(id=id)
