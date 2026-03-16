def test_root_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
