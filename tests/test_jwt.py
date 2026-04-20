import requests

BASE_URL = "http://127.0.0.1:8000"

def test_jwt_auth_flow():
    login = requests.post(f"{BASE_URL}/login", json={
        "email": "test@example.com",
        "password": "testpassword"
    })

    assert login.status_code == 200

    token = login.json().get("access_token")
    assert token is not None

    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert res.status_code == 200