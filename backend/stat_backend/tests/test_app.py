from app import create_app


def test_first():
    assert True


def test_health():
    app = create_app()
    response = app.test_client().get("/api/healthz")
    assert response.status_code == 200
    assert response.data == b'"OK"\n'
