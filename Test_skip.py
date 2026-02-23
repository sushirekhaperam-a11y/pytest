#skip - if defects are there
#skip - if testcases are absolute
#skip - mobile, window -OS dependencies
#skip - browser -FF,IE,chrome

import pytest


def testcase1():
    print("testecase1 is executed")

@pytest.mark.skip
def testcase2():
    print("testcase2 is executed")


def test_case3():
    print("testcase 3 is excecuted")
@pytest.mark.skip
def openbrowser():
    print("open the browser")

