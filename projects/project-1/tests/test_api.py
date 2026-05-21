from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={"text_to_analyze": "Investir no produto XPTO com risco"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "is_compliant" in data
    assert "reason" in data
    assert "mentioned_products" in data


def test_analyze_validation():
    response = client.post(
        "/analyze",
        json={"text_to_analyze": "curto"}
    )

    assert response.status_code == 422