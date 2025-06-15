import runpy

def test_frontend_runs():
    try:
        runpy.run_path("frontend/app.py")
        assert True
    except Exception as e:
        pytest.fail(f"El frontend no se ejecuta correctamente: {e}")
