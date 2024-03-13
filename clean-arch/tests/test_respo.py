from app.repository import UserRepository

ur = UserRepository()


def test_ur() -> None:
    user_id = "1"
    username = "viktor"

    _username = ur.get(user_id)

    assert username.lower() == _username.name.lower()
    return
