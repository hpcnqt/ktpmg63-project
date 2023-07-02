from flask import Blueprint, render_template, request, session, redirect, url_for
import time
import view.account as vw_account

authentication_bp = Blueprint('authentication', __name__)


def is_authenticated():
    return session.get('is_authenticated')


@authentication_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        login_user = vw_account.login(username=username, password=password)
        if login_user[0]:
            session['username'] = login_user[2]
            session['is_authenticated'] = True

            time.sleep(1)
            return redirect(url_for('dashboard.layout'))

    time.sleep(1)
    return render_template('authentication/login.html')


@authentication_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_authenticated', None)

    time.sleep(1)
    return redirect(url_for('authentication.login'))