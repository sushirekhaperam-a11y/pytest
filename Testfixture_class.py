import pytest
class Testlogin:
    @pytest.mark.usefixtures("dbconnection")
    def test_login(self):
        print("enter the login ")
        print("enter the username")
        print("enter the password")
    def test_logout(self):
        print("user is logged out")
