from flask import Blueprint, render_template, request, redirect
from bankapp.logic import login


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/login', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        user = login(
            email=request.form.get('email'),
            password=request.form.get('password')
        )

        if user:
            return redirect('/profile/{}'.format(str(user.id)))
    return render_template('login.html')
