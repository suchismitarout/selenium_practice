import pytest

@pytest.mark.run(order=2)
def test_demoA(onetimesetUp):
    print("This is A test method")

@pytest.mark.run(order=1)
def test_demoB(onetimesetUp):
    print("This is B test method")

@pytest.mark.run(order=4)
def test_demoC(onetimesetUp):
    print("This is C test method")

@pytest.mark.run(order=3)
def test_demoD(onetimesetUp):
    print("This is D test method")