import modal.population as modal


def generate_id():
    addition = modal.total()
    if addition < 10000:
        original_string = '0060020810000'
        result = int(original_string) + addition + 1
        return str(result).zfill(len(original_string))


def find_all():
    return modal.find_all()


def find_by_id(id):
    return modal.find_by_id(id)


def find_by_household_id(id):
    return modal.find_by_household(id=id)


def update_household_id(id, new_household_id):
    return modal.update_household_id(id=id, new_household_id=new_household_id)


def create(population):
    return modal.insert(population=population)


def update(population):
    return modal.update(population=population)
