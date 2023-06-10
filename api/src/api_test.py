import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"message": "Api is working"}

def test_recommend_movies():
    username = "john"
    response = client.get(f"/recommend-movies/{username}")
    assert response.status_code == 200
    assert "titles" in response.json()
