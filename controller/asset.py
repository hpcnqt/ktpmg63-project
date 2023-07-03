import time
import view.asset as view
from flask import Blueprint, render_template, redirect, url_for, request

from controller.authentication import is_authenticated
from modal.asset import Asset

asset_bp = Blueprint('asset', __name__, url_prefix='/asset')


@asset_bp.route('/', methods=['GET', 'POST'])
def layout():
    time.sleep(1)
    if is_authenticated():
        assets = view.find_all()
        return render_template('culturalhouse/asset/layout.html', len=len(assets), assets=assets)
    else:
        return redirect(url_for('authentication.login'))
    

@asset_bp.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    time.sleep(1)
    
    if is_authenticated():
        asset = view.find_by_id(id)

        if request.method == 'POST':
            
            new_name = request.form.get('assetName')
            new_qty = request.form.get('assetQty')

            updated_asset = Asset(id=id, name=new_name, qty=new_qty)
            view.update(updated_asset)
            return redirect(url_for('asset.detail', id=id))
        
        return render_template('culturalhouse/asset/edit.html', asset=asset)
    else:
        return redirect(url_for('authentication.login'))


@asset_bp.route('/asset/detail/<id>')
def detail(id):
    time.sleep(1)

    if is_authenticated():
        asset = view.find_by_id(id)

        return render_template('culturalhouse/asset/detail.html', asset=asset)
    else:
        return redirect(url_for('authentication.login'))

@asset_bp.route('/add', methods=['GET', 'POST'])
def add():
    time.sleep(1)

    if is_authenticated():  
        if request.method == "POST":
            new_id = request.form.get('assetId')
            new_name = request.form.get('assetName')
            new_qty = request.form.get('assetQty')

            new_asset = Asset(id = new_id, name = new_name, qty = new_qty)
            view.create(new_asset)
            return redirect(url_for('asset.detail', id = new_id))

        return render_template('culturalhouse/asset/add.html', assetId = view.generate_id())
    else:
        return render_template(url_for('authentication.login'))
