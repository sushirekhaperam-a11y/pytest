import pytest
#request - pytest object that contains the information about who is calling the fixture and with what data
@pytest.fixture(params = ["chrome","firefox"])
def browser(request):
    print("Current browser:",request.param)
    return request.param
def test_browser(browser):
    assert browser in ["chrome","firefox"]

#selecting even or odd numbers
@pytest.fixture(params=[1,2,3,4,5])
def even_odd(request):
    print("even odd:",request.param)
    return request.param
def test_evenodd(even_odd):
    if even_odd%2 ==0:
        print(f"{even_odd} is even")
        assert even_odd %2 == 0
    else:
        print(f"{even_odd} is odd")
        assert even_odd != 0




