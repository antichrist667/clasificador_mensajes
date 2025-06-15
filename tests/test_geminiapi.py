from unittest.mock import patch
from app.geminiapi import clasificar_mensaje

@patch("app.geminiapi.model.generate_content")
def test_clasificar_mensaje_mock(mock_generate):
    mock_generate.return_value.text = "Urgente"
    resultado = clasificar_mensaje("Esto es una emergencia")
    assert resultado in ["Urgente", "Moderado", "Normal"]
