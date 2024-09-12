import pytest

#Fixtures allow setting up preconditions for tests
@pytest.fixture
def setup():
    print("This is for presetup")

def test_add(setup):
    x=10
    y=20
    assert x < y

# tmpdir : Provides a temporary directory for writing and reading files during the test.
# The directory is automatically deleted after the test.
def test_write_file(tmpdir):
    file = tmpdir.join("sample.txt")
    file.write("Hello, pytest!")
    assert file.read() == "Hello, pytest!"


def test_write_file1(tmpdir):
    file=tmpdir.join("sample.txt")
    file.write("Happy coding with python")
    assert file.read() == "Happy coding with python"


