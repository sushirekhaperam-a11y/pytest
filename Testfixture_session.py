#session - runs once per the pytest
#used in global configuration
import pytest

from PythonProgramming.pytest.conftest import setupsession


@pytest.mark.usefixtures('setupsession')
def test_case1():
    print("testcase1")
def test_case2():
    print("testcase2")