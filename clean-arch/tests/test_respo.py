from app.stores import UserInMemoryRepository
from core.entities import User

ur = UserInMemoryRepository()


def test_ur() -> None:
    user = User(id="1", name="viktor")

    expected_user = ur.get(user.id)

    assert user.name.lower() == expected_user.name.lower()
    return None
