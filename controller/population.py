import time
from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request
from controller.authentication import is_authenticated
from modal.population import Population
import view.population as view

population_bp = Blueprint('population', __name__)


@population_bp.route('/population', methods=['GET', 'POST'])
def layout():
    time.sleep(1)

    if is_authenticated():
        if request.method == 'POST':
            id = request.form.get('populationSearch')
            population = view.find_by_id(id)
            populations = [population['population']]
            return render_template('population/layout.html', len=len(populations), populations=populations)
        else:
            populations = view.find_all()
            return render_template('population/layout.html', len=len(populations), populations=populations)
    else:
        return redirect(url_for('authentication.login'))


@population_bp.route('/population/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    time.sleep(1)

    if is_authenticated():
        population = view.find_by_id(id)

        if request.method == 'POST':
            population_id = request.form.get('populationId')
            full_name = request.form.get('fullName')
            other_name = request.form.get('otherName')
            date_of_birth = request.form.get('dateOfBirth')
            born_location = request.form.get('bornLocation')
            gender = int(request.form.get('gender'))
            ethnic = request.form.get('ethnic')
            religion = request.form.get('religion')
            id_number = request.form.get('idNumber')
            passport_number = request.form.get('passportNumber')

            updated_population = Population(id=population_id,
                                            full_name=full_name,
                                            other_name=other_name,
                                            date_of_birth=date_of_birth,
                                            born_location=born_location,
                                            gender=gender,
                                            ethnic=ethnic,
                                            religion=religion,
                                            id_number=id_number,
                                            pp_number=passport_number,
                                            updated_date=datetime.today().strftime("%Y-%m-%d"))
            view.update(updated_population)
            return redirect(url_for('population.detail', id=population_id))

        return render_template('population/edit.html', population=population)
    else:
        return redirect(url_for('authentication.login'))


@population_bp.route('/population/detail/<id>')
def detail(id):
    time.sleep(1)

    if is_authenticated():
        population = view.find_by_id(id)

        return render_template('population/detail.html', population=population)
    else:
        return redirect(url_for('authentication.login'))


@population_bp.route('/population/add', methods=['GET', 'POST'])
def add():
    time.sleep(1)

    if is_authenticated():
        if request.method == 'POST':
            population_id = request.form.get('populationId')
            full_name = request.form.get('fullName')
            other_name = request.form.get('otherName')
            date_of_birth = request.form.get('dateOfBirth')
            born_location = request.form.get('bornLocation')
            gender = request.form.get('gender')
            ethnic = request.form.get('ethnic')
            religion = request.form.get('religion')
            id_number = request.form.get('idNumber')
            passport_number = request.form.get('passportNumber')

            new_population = Population(id=population_id,
                                            full_name=full_name,
                                            other_name=other_name,
                                            date_of_birth=date_of_birth,
                                            born_location=born_location,
                                            gender=gender,
                                            ethnic=ethnic,
                                            religion=religion,
                                            id_number=id_number,
                                            pp_number=passport_number,
                                            updated_date=datetime.now().strftime("%Y-%m-%d"))
            view.create(new_population)
            return redirect(url_for('population.detail', id=population_id))

        return render_template('population/add.html', populationId = view.generate_id())
    else:
        return redirect(url_for('authentication.login'))
