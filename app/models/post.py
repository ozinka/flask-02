from datetime import datetime, UTC
from ..extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    subject = db.Column(db.String(80))
    student = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now(UTC))
