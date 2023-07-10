from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..main import main

client = TestClient(app)

def test_is_alive():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

test_is_alive()