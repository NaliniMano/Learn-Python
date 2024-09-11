import pytest

#Fixtures allow setting up preconditions for tests
@pytest.fixture
def setup():
    print("This is for presetup")

def test_add(setup):
    x=10
    y=20
    assert x<y


