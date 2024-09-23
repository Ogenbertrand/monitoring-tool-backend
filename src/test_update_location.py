import pytest
import requests
from update_location import get_users, fetch_latest_location, update_user_location, update_all_user_locations

class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def json(self):
        return [{'id': 1}]

    def raise_for_status(self):
        pass

@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', lambda url: MockResponse(200))
    monkeypatch.setattr(requests, 'put', lambda url, json: MockResponse(200))

def test_get_users(mock_requests):
    users = get_users()
    assert len(users) == 1

def test_update_user_location(mock_requests):
    update_user_location(1, {'latitude': '12.34', 'longitude': '56.78'})

def test_update_all_user_locations(mock_requests):
    update_all_user_locations()
