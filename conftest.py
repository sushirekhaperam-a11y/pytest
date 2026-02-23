
import pytest

@pytest.fixture
def simple_data():
    return 45


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

@pytest.fixture()
def api_url():
    return  "https://api.example.com"

@pytest.fixture(scope = 'function')
def openbrowser():
    # precondition
    print("open the browser")

@pytest.fixture(scope = 'function')
def closebrowser():
     # post condition
    print("closing the browser")
@pytest.fixture(scope = 'class')
def dbconnection():
    # when we use yield  -automatic teardown is happening
    print("open the dbconnection") # code before the yield - setup
    yield
    print("close the dbconnection") # code after the yield - teardown
@pytest.fixture
def setup():
    print("setup")
    return "data"
# when we are using the return automatic teardown will not happen

@pytest.fixture(scope = 'module')
def setupapi():
    # when we use yield  -automatic teardown is happening
    print("authorize the username and password") # code before the yield - setup
    yield
    print("unauthorize the username and password")
@pytest.fixture(scope = 'session')
def setupsession():
    # when we use yield  -automatic teardown is happening
    print("authentication token  started") # code before the yield - setup
    yield
    print("session finished")

#fixture dependency
@pytest.fixture
def fixture_a():
    return "Data from A"
@pytest.fixture
def fixture_b(fixture_a):
    return f"{fixture_a}"+"Data from B"

@pytest.fixture
def base_url():
    return "URL has created"
@pytest.fixture
def auth_token(base_url):
    return f"{base_url}"+"generating auth token"
@pytest.fixture
def user(auth_token):
    return f"{auth_token}"+"creating test user"

