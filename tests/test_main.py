# tests/test_geminiapi.py
import pytest
from app.geminiapi import clasificar_mensaje

def test_clasificar_mensaje_exists():
    assert callable(clasificar_mensaje)
