import pytest

@pytest.mark.usefixtures("setupapi")
def test_one():
    print("test one")
def test_two():
    print("test two")