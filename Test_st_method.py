#used inside the classes
#runs before and after the test methods inside the class
#In case of inheritance setup and teardown is applied
import pytest
class Testclass1:
    def setup_class(cls):
        print("API authorization is open")

    def teardown_class(cls):
        print("API authorization is closed")

    def setup_method(method):
        print("openthe is browser")

    def teardown_method(method):
        print("browser is  closed")

    def testcase1(self):
        print("testecase1 is executed")

    def testcase2(self):
        print("testcase2 is executed")

    def test_case3(self):
        print("testcase 3 is excecuted")


class Testclass2:
    def testcase1(self):
        print("testecase1 is executed")

    def testcase2(self):
        print("testcase2 is executed")

    def test_case3(self):
        print("testcase 3 is excecuted")

class Testclass1:
    def setup_class(cls):
        print("API authorization is open")

    def teardown_class(cls):
        print("API authorization is closed")

    def setup_method(method):
        print("openthe is browser")

    def teardown_method(method):
        print("browser is  closed")

    def testcase1(self):
        print("testecase1 is executed")

    def testcase2(self):
        print("testcase2 is executed")

    def test_case3(self):
        print("testcase 3 is excecuted")


class Testclass2(Testclass1):
    def testcase1(self):
        print("testecase1 is executed")
    @pytest.mark.regression
    def testcase2(self):
        print("testcase2 is executed")
    @pytest.mark.sanity
    def test_case3(self):
        print("testcase 3 is excecuted")

