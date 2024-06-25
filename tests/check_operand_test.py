from verify_file import check_filename
from verify_operand import check_operation


def test_check_filename(monkeypatch):
    # Simuler une entrée utilisateur
    monkeypatch.setattr('builtins.input', lambda _: 'test.csv')
    assert check_filename() == 'test.csv'


def test_check_operation(monkeypatch):
    # Simuler une entrée utilisateur
    monkeypatch.setattr('builtins.input', lambda _: '+')
    assert check_operation() == '+'
