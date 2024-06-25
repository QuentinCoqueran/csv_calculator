from result_displayer import display_result
from io import StringIO
import sys


def test_display_result():
    numbers = [1, 2, 3, 4, 5]
    operation = '+'
    result = 15

    captured_output = StringIO()
    sys.stdout = captured_output

    display_result(numbers, operation, result)

    sys.stdout = sys.__stdout__  # Rétablir la sortie standard

    expected_output = "1 + 2 + 3 + 4 + 5 = 15\n-------\ntotal = 15 (+)\n"
    assert captured_output.getvalue() == expected_output
