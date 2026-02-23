#parameterization -
#@pytest.mark.parametrize

#no parametrize
def test_add1():
    assert  2+3 == 5
def test_add2():
    assert 6+6 == 12

#parameterize
import pytest
@pytest.mark.parametrize("a,b,result",[(2,3,5),(4,5,9),(6,7,13)])
def test_add(a,b,result):
    assert a+b == result
@pytest.mark.parametrize("number",[1,2,3,4,5,6])
def test_add3(number):
    assert (number%2) == 0

#dictionary items
@pytest.mark.parametrize("payload",[{"name":"john","age":15}])
def test_create_user(payload):
    assert payload["age"] > 18



