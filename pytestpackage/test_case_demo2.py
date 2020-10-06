import pytest

@pytest.yield_fixture()
def setUp():
    print("This will run before every method")
    yield
    print("This will run after every method")

def test_methodA(setUp):
    print("This is first test method")

def test_methodB(setUp):
    print("This is second test method")

