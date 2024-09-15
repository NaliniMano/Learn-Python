import pytest

#request fixture is used to access the name of the test currently being executed.
# Based on the test name, different setups are applied dynamically.
@pytest.fixture
def dynamic_setup(request):
    # Accessing the name of the test function
    test_name = request.node.name

    if test_name == "test_one":
        return "Setup for test one"
    elif test_name == "test_two":
        return "Setup for test two"
    else:
        return "Default setup"

def test_one(dynamic_setup):
    print(dynamic_setup)  # This will print "Setup for test one"
    assert dynamic_setup == "Setup for test one"

def test_two(dynamic_setup):
    print(dynamic_setup)  # This will print "Setup for test two"
    assert dynamic_setup == "Setup for test two"

def test_three(dynamic_setup):
    print(dynamic_setup)  # This will print "Default setup"
    assert dynamic_setup == "Default setup"
