import pytest

@pytest.mark.smoke
def test_program_greeting():
    msg = "Hi, how are you!!"
    print(msg)

@pytest.mark.skip
def test_program_good():
    print("you are doing good")

@pytest.mark.xfail
def test_ask_program():
    print("Hi whats up? What doing good, right!")

