import pytest
from app import app, db, UserLocation

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.create_all()
    yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_save_location(client):
    response = client.post('/api/location', json={
        'ip': '123.123.123.123',
        'city': 'Test City',
        'region': 'Test Region',
        'country': 'Test Country',
        'latitude': '0.0',
        'longitude': '0.0'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Location saved'
