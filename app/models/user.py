from ..extensions import db, login_manager
from datetime import datetime, UTC
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), default='user')
    name = db.Column(db.String(50), unique=True, nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(UTC))
    avatar = db.Column(db.String(200))
