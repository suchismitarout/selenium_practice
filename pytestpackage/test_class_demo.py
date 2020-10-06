import pytest
from pytestpackage.class_to_test import SomeclassTotest

@pytest.mark.usefixtures("onetimesetUp")
class TestClassDemo():
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = SomeclassTotest(10)

    def test_methodA(self):
        result = self.abc.total_sum(5,15)
        assert result == 30
        print("This is test method A")

    def test_methodB(self):
        result = self.abc.total_sum(5,15)
        assert result > 30
        print("This is test method B")

