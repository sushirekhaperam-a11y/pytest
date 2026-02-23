#Function level setup and tear down - these run before and after each test function

#set up at the function
def setup_function(function):
    print("opening the browser")

#tear down up at the function level
def teardown_function(function):
    print("closing the browser")

def testcase1():
    print("testecase1 is executed")
def testcase2():
    print("testcase2 is executed")
def test_case3():
    print("testcase 3 is excecuted")
def openbrowser():
    print("open the browser")