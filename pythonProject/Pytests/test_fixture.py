import pytest
@pytest.mark.usefixtures("test_callingClass")
class Test_caller:
    def test_numberOne(self):
        print("Hi, I'm under the class and I will execute with the test number")
    def test_numberTwo(self):
        print("Hi, I'm under the class and I will execute with the test number")
    def test_numberThree(self):
        print("Hi, I'm under the class and I will execute with the test number")
    def test_numberFour(self):
        print("Hi, I'm under the class and I will execute with the test number")