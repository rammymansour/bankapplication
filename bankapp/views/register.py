from flask import Blueprint, render_template, request, redirect
from bankapp.logic import register_user


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        user = register_user(
            email=request.form.get('email'),
            firstname=request.form.get('firstname'),
            lastname=request.form.get('lastname'),
            password=request.form.get('password'),
        )

        if user:
            return redirect('/login?user_id={}'.format(str(user.id)))
    return render_template('register.html')
