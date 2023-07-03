import time
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request
from controller.authentication import is_authenticated
import view.household as view
import view.population as pview
from modal.household import Household

household_bp = Blueprint('household', __name__)


@household_bp.route('/household', methods=['GET', 'POST'])
def layout():
    time.sleep(1)
    if is_authenticated():
        if request.method == 'POST':
            id = request.form.get('householdSearch')
            household = view.find_by_id(id)
            households = [household['household']]
            return render_template('household/layout.html', len=len(households), households=households)
        else:
            households = view.find_all()
            return render_template('household/layout.html', len=len(households), households=households)
    else:
        return redirect(url_for('authentication.login'))


@household_bp.route('/household/detail/<id>')
def detail(id):
    time.sleep(1)

    if is_authenticated():
        household = view.find_by_id(id)

        return render_template('household/detail.html', household=household['household'],
                               members=household['members'],
                               len=len(household['members']))
    else:
        return redirect(url_for('authentication.login'))


@household_bp.route('/household/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    time.sleep(1)

    if is_authenticated():
        household = view.find_by_id(id)

        if request.method == 'POST':
            household_id = request.form.get('householdId')
            print(household_id)
            house_number = request.form.get('houseNumber')
            street = request.form.get('street')
            commune = request.form.get('commune')
            district = request.form.get('district')
            province = request.form.get('province')
            register_date = request.form.get('registerDate')
            updated_date = request.form.get('updatedDate')
            householder_id = request.form.get('householderId')

            updated_household = Household(id=household_id,
                                          house_number=house_number,
                                          street_hamlet=street,
                                          commune_ward=commune,
                                          city_district_town=district,
                                          province=province,
                                          register_date=register_date,
                                          updated_date=updated_date,
                                          householder_id=householder_id)

            print(updated_household.id)
            view.update(updated_household)
            return redirect(url_for('household.detail', id=household_id))

        return render_template('household/edit.html', household=household['household'],
                               members=household['members'],
                               len=len(household['members']))
    else:
        return redirect(url_for('authentication.login'))


@household_bp.route('/household/add', methods=['GET', 'POST'])
def add():
    time.sleep(1)

    if is_authenticated():
        if request.method == 'POST':
            household_id = request.form.get('householdId')
            house_number = request.form.get('houseNumber')
            street = request.form.get('street')
            commune = request.form.get('commune')
            district = request.form.get('district')
            province = request.form.get('province')
            register_date = request.form.get('registerDate')
            updated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            householder_id = request.form.get('householderId')

            new_household = Household(id=household_id,
                                      house_number=house_number,
                                      street_hamlet=street,
                                      commune_ward=commune,
                                      city_district_town=district,
                                      province=province,
                                      register_date=register_date,
                                      updated_date=updated_date,
                                      householder_id=householder_id)
            # print(new_household.id, new_household.householder_id)
            view.create(new_household)
            pview.update_household_id(id=householder_id, new_household_id=household_id)
            return redirect(url_for('household.detail', id=household_id))

        return render_template('household/add.html', householdId=view.generate_id(),
                               today=datetime.today().strftime("%Y-%m-%d"))
    else:
        return redirect(url_for('authentication.login'))
