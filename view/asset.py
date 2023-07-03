import modal.asset as modal

def generate_id():
    addition = modal.total()
    if addition < 10000:
        original_string = '0'
        result = int(original_string) + addition + 1
        return str(result).zfill(len(original_string))

def find_all():
    return modal.find_all()

def find_by_name(name):
    return modal.find_by_name(name)

def find_by_id(id):
    return modal.find_by_id(id)

def total():
    return modal.total()

def update(asset):
    return modal.update(asset=asset)

def create(asset):
    return modal.insert(asset=asset)
