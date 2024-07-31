import pytest
from app.utils import print_it

def test_print_it(capsys):
    test_text = "Hello, world!"
    print_it(test_text)
    captured = capsys.readouterr()
    assert captured.out.strip() == test_text