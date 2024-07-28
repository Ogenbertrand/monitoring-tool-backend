from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), nullable=True)
    city = db.Column(db.String(100))
    region = db.Column(db.String(100))
    country = db.Column(db.String(100))
    loc = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    