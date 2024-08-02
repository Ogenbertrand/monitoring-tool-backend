from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, UserLocation
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/api/location', methods=['POST'])
def save_location():
    data = request.get_json()
    ip = data.get('ip')

    if not ip or not data.get('city') or not data.get('region') or not data.get('country') or not data.get('latitude') or not data.get('longitude'):
        return jsonify({"message": "Invalid request"}), 400

    existing_location = UserLocation.query.filter_by(ip=ip).first()
    if existing_location:
        existing_location.city = data.get('city')
        existing_location.region = data.get('region')
        existing_location.country = data.get('country')
        existing_location.latitude = data.get('latitude')
        existing_location.longitude = data.get('longitude')
        db.session.commit()
        return jsonify({"message": "Location updated"}), 200
    else:
        location = UserLocation(
            ip=ip,
            city=data.get('city'),
            region=data.get('region'),
            country=data.get('country'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude')
        )
        db.session.add(location)
        db.session.commit()
        return jsonify({"message": "Location saved"}), 201

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
