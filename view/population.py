import modal.population as modal


def find_all():
    return modal.find_all()


def find_by_id(id):
    return modal.find_by_id(id)


def find_by_household_id(id):
    return modal.find_by_household(id=id)


def update_household_id(id, new_household_id):
    return modal.update_household_id(id=id, new_household_id=new_household_id)
