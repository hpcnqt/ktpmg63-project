from flask import Blueprint, render_template


asset_bp = Blueprint('asset', __name__, url_prefix='/asset')


@asset_bp.route('/')
def layout():
    return render_template('culturalhouse/asset/layout.html')