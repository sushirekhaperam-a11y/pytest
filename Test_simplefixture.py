# Fixture - is a piece of code that run befre the test cases and after the testcases

import pytest
@pytest.fixture
def simple_data():
    assert 45

def test_case1(simple_data):
    assert simple_data == 45

@pytest.fixture
def api_url():
    return "http://api.example.com"
def testcase2(api_url):
    assert "http" in api_url