import pytest

@pytest.fixture()
def setUp():
    print("This runs before each test method")
    yield
    print("This tuns after each test method")

@pytest.fixture(scope="class")
def onetimesetUp():
    print("This runs once before test method")
    yield
    print("This tuns once after test method")