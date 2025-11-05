from app import create_app


def test_home_status():
    app = create_app()
    client = app.test_client()
    resp = client.get('/inventory/')
    assert resp.status_code in [200, 401]