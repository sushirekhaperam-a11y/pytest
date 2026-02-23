import pytest

@pytest.mark.usefixtures("openbrowser")
def test_login():
    print("enter the login ")
    print("enter the username")
    print("enter the password")

@pytest.mark.usefixtures("closebrowser")
def test_logout():
    print("user is logged out")
