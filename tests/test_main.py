from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_clasificar_endpoint():
    with patch("app.geminiapi.clasificar_mensaje", return_value="Moderado"):
        response = client.post("/clasificar", json={"texto": "Mensaje de prueba"})
        assert response.status_code == 200
        assert response.json()["clasificación"] in ["Urgente", "Moderado", "Normal"]
