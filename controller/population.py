import time

from flask import Blueprint, render_template, redirect, url_for, request
from controller.authentication import is_authenticated
import view.population as view

population_bp = Blueprint('population', __name__)


@population_bp.route('/population', methods=['GET', 'POST'])
def layout():
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

@population_bp.route('/population/add')
def add():
    if is_authenticated():
        return render_template('population/add.html')
    else:
        return redirect(url_for('authentication.login'))


@population_bp.route('/population/edit/<id>')
def edit(id):
    if is_authenticated():
        population = view.find_by_id(id)
        return render_template('population/edit.html', population=population)
    else:
        return redirect(url_for('authentication.login'))
