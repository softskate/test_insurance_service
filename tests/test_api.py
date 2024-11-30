from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_insurance():
    response = client.get(
        "/insurance/calculate",
        params={"cargo_type": "Glass", "declared_value": 1000, "date": "2020-06-15"}
    )
    assert response.status_code == 200
    assert "insurance_cost" in response.json()

def test_create_tariff():
    payload = {
        "cargo_type": "Electronics",
        "rate": 0.02,
        "effective_date": "2024-01-01"
    }
    response = client.post("/tariffs/", json=payload)
    assert response.status_code == 200
    assert response.json()["cargo_type"] == "Electronics"

def test_delete_tariff():
    response = client.delete("/tariffs/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Tariff 1 deleted"
