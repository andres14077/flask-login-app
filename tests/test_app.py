import pytest
from flask_login_app.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to SecureBank" in response.data

def test_successful_login(client):
    response = client.post("/login", data={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert b"Login successful!" in response.data

def test_failed_login(client):
    response = client.post("/login", data={"username": "user", "password": "wrongpassword"})
    assert response.status_code == 401
    assert b"Invalid credentials!" in response.data
