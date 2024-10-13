from source.math_opt import addition,subtraction

def test_addition():
    assert addition(1,2) == 3
    assert addition(0, 0) == 0
    assert addition(-1, 1) == 0


def test_subtraction():
    assert subtraction(1, 2) == -1
    assert subtraction(0, 0) == 0
    assert subtraction(-1, 1) == -2

    