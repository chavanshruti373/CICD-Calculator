from app.calculator import add, subtraction, multiply, divide

def test_add():
    assert add(2, 3) == 5


def subtraction():
    assert subtraction(5, 2) == 3

def test_multiply():
    assert multiply(2, 4) == 8


def test_divide():
    assert divide(10, 2) == 5
