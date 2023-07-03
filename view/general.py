import modal.general as modal
import modal.population as p
import modal.household as h


class Information:
    general = modal.find_general()

    owner = general.owner.strip()
    location = general.location.strip()
    from_year = general.from_year
    to_year = general.to_year

    totalPopulation = p.total()
    totalHousehold = h.total()