import modal.event
import modal.event as modal_event
import modal.department as modal_department

def generate_id():
    addition = modal.total()
    if addition < 10000:
        original_string = '0'
        result = int(original_string) + addition + 1
        return str(result).zfill(len(original_string))

def find_all():
    result = dict()
    result['event'] = modal_event.find_all()
    result['department'] = modal_department.find_all()
    return result


def find_by_id(id):
    return modal_event.find_by_id(id=id)

def create(event):
    return modal.insert(event=event)
