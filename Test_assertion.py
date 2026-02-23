#basic assertion
#Hard assertion  -  this will stop the execution of the test cases
#soft assertion - this will continue to run if the assertion fails

def test_add():
    result = 2+3
    assert result == 5

#checking true or false
def test_boolean():
    assert True
    assert not False

#none value
def test_none():
    value = None
    assert value is None

#list
def test_list():
    list = ["banana","apple","orange"]
    assert "banana" in list
#dictionary
def test_dict():
    dict = {"name":"sunil","password":"admin"}
    assert dict["password"]  == "admin"
#comparing two list
def test_twolist():
    assert [1,2,3] == [1,2,3]

#assertion with custom message
def test_custom():
    value = 10
    assert value == 10 ," result should be 10"
#soft assertion
import pytest_check as check
def test_multiples():
    check.equal(1,3)
    check.equal(3,3)


