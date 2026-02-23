import pytest
from Test_simplefixture import api_url
def test_case1():
    print("Testcase1 is executed")
def test_case2():
    print("Testcase2 is executed")
def test_case3():
    print("Testcase3 is executed")
def test_case4():
    print("Testcase4 is executed")
def test_login():
    print("login test is executed")

def testcase2(api_url):
    assert "http" in api_url