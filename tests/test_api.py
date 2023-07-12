from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_is_alive():
    response = client.get("/alive")
    assert response.status_code == 200
    assert response.json() == {"Me": "Hi"}

test_is_alive()