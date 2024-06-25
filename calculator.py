import operator
from functools import reduce


def calculate(numbers, operation):
    if operation == '+':
        return sum(numbers)
    elif operation == '*':
        return reduce(operator.mul, numbers)
    else:
        raise ValueError('Operation not supported')