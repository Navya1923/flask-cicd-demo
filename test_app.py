from app import app


def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200


def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200


def test_ready():
    r = app.test_client().get("/ready")
    assert r.status_code == 200