#xfail is a marker used to indicate that a test is expected to fail due to a known issue (e.g., a bug or an unimplemented feature)
import pytest
import sys
@pytest.mark.xfail(reason = "Known bug in third party library")
def test_function_with_bug():
    assert (1+1) == 3 # This assertion will fail as expected

def testcase1():
    print("testecase1 is executed")

@pytest.mark.sanity
def testcase2():
    print("testcase2 is executed")

@pytest.mark.regression
def test_case3():
    print("testcase 3 is excecuted")

# x fail with a condition
@pytest.mark.xfail(sys.platform == "win32",reason ="Bug on windows")
def test():
    print("test on windows")
#xfail fail only for windows
#xfail for strict = true ,
@pytest.mark.xfail(strict = True ,reason ="Bug #123 is not fixed yet")
def test_function():
    print("fail")
#the test case should fail mandatiorly