from app.operations import add, multiply, divide

def test_add():
    assert add(2,2) == 4

def test_multiplication():
    assert multiply(2,2) == 4

def test_division():
    assert divide(2,2) == 1