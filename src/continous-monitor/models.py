from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<UserLocation {self.ip} - {self.city}, {self.country}>'
