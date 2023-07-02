import modal.household as modal
import view.population as population_view


def generate_id():
    addition = modal.total()
    if addition < 10000:
        original_string = '006002081000'
        result = int(original_string) + addition + 1
        return str(result).zfill(len(original_string))


def find_all():
    return modal.find_all()


def find_by_id(id):
    result = dict()
    result['household'] = modal.find_by_id(id)
    result['members'] = population_view.find_by_household_id(id)
    return result


def update(household):
    return modal.update(household=household)


def create(household):
    return modal.insert(household=household)
