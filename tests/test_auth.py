def test_register_returns_201(client):
    resp = client.post("/api/auth/register", json={
        "email": "new@example.com",
        "display_name": "New User",
        "password": "securepass123",
    })
    assert resp.status_code == 201
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_register_duplicate_email_returns_409(client):
    payload = {
        "email": "dup@example.com",
        "display_name": "User",
        "password": "securepass123",
    }
    client.post("/api/auth/register", json=payload)
    resp = client.post("/api/auth/register", json=payload)
    assert resp.status_code == 409


def test_login_success(client):
    client.post("/api/auth/register", json={
        "email": "login@example.com",
        "display_name": "Login User",
        "password": "securepass123",
    })
    resp = client.post("/api/auth/login", json={
        "email": "login@example.com",
        "password": "securepass123",
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_bad_password(client):
    client.post("/api/auth/register", json={
        "email": "bad@example.com",
        "display_name": "Bad Pass",
        "password": "securepass123",
    })
    resp = client.post("/api/auth/login", json={
        "email": "bad@example.com",
        "password": "wrongpassword",
    })
    assert resp.status_code == 401


def test_me_returns_profile(client, auth_headers):
    resp = client.get("/api/auth/me", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == "test@example.com"
    assert data["display_name"] == "Test User"
    assert "id" in data
    assert "created_at" in data


def test_me_without_token(client):
    resp = client.get("/api/auth/me")
    assert resp.status_code == 401
