import pytest

@pytest.fixture()
def setUp():
    print("This will run before every method")

def test_method1(setUp):
    print("This is first method")

def test_method2():
    print("This is second method")


