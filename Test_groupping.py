#grouping - set of testcases run together - issues fix in that module pytest -m regression -v -s  --html=test_groupingp.html
import pytest

@pytest.mark.db
def testcase1():
    print("testecase1 is executed")

@pytest.mark.sanity
def testcase2():
    print("testcase2 is executed")

@pytest.mark.regression
def test_case3():
    print("testcase 3 is excecuted")

