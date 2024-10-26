import pytest

@pytest.fixture(scope="class")
def test_callingClass():
    print("I'm first")
    yield
    print("I'm last")

@pytest.fixture()
def test_giving_data():
    print("I'm in conftest file")
    return ["one", "two", "three", "four", "five","six"]

@pytest.fixture(params = [("one","two","three"),("five","six"),("seven","Eight")])
def givingData(request):
    return request.param
