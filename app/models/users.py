from ..extensions import db
from datetime import datetime, UTC

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), default='user')
    name = db.Column(db.String(50), unique=True, nullable=False)
    login =db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(200), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(UTC))
    avatar = db.Column(db.String(200))

