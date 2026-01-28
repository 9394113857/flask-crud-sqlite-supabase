from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
