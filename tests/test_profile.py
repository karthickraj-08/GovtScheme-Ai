from pydantic import ValidationError
from models.profile import UserProfile


def test_profile_normalization():
    profile = UserProfile(name=" Test ", state="  Tamil   Nadu ", age=21)
    assert profile.state == "Tamil Nadu"


def test_invalid_age():
    try:
        UserProfile(age=121)
        assert False
    except ValidationError:
        assert True
