from flask import Blueprint, render_template, redirect
from bankapp.models.Person import Person
from bson.objectid import ObjectId

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/profile/<user_id>')
def show(user_id):
    person = Person.objects(id=ObjectId(user_id)).get()
    if not person:
        return redirect('/')

    return render_template('profile.html', person=person)
