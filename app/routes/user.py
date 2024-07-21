from flask import Blueprint
from ..extensions import db
from ..models.users import User

user = Blueprint('user', __name__)

@user.route('/user/<name>')
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f'User {name} created'