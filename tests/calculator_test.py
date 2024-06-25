from calculator import calculate


def test_calculate_sum():
    numbers = [1, 2, 3, 4, 5]
    assert calculate(numbers, '+') == 15


def test_calculate_product():
    numbers = [1, 2, 3, 4, 5]
    assert calculate(numbers, '*') == 120
