from _datetime import datetime, UTC
from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80))
    teacher = db.Column(db.String(80))
    student = db.Column(db.String(80))
    date = db.Column(db.DateTime, default=datetime.now(UTC))
