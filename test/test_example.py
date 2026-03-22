from src.math_oper import add

def test_add():
    assert add(2, 3) == 5
    assert add(1,1) == 2
    assert add(0, 0) == 0

def test_subtract():
    from src.math_oper import subtract
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0

def test_multiply():
    from src.math_oper import multiply
    assert multiply(2, 3) == 6
    assert multiply(4, 5) == 20
    assert multiply(0, 10) == 0