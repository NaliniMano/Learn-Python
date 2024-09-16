import pytest
@pytest.fixture(scope="function",autouse=True)
def setup_module():
    print("Setup module-level fixture")

def test_1():
    print("This is test")


