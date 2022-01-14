from passlib.utils.compat import nextgetter
from jose import jwt
from starlette.responses import Response
from app import schemas
from app.config import settings
import pytest



def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == 'Ircya-Kaban4uk'
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "shashlik@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    print(new_user.json())
    assert new_user.email == "shashlik@gmail.com"
    assert res.status_code == 201


def test_login_user(test_user, client):
    # login user is dependent now on client and test_user
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    # decoding jwt
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    # extra validation with token
    # to validate we going to decode token
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@gmail.com", "password123", 403),
    ("kaban@gmail.com", "wrongpassword", 403),
    ("wrongemail@gmail.com", "wrongpassword", 403),
    (None, "password123", 422),
    # 422 is error for missing fields
    ("kaban@gmail.com", None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code
    # you can validate anything, this is just focus validation for status_code
    # assert res.json().get('detail') == 'Invalid Credentials'