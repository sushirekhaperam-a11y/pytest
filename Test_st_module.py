#setup and teardown - module level - runs once per module(file)
#use module level set up and tear down when you want to execute the setup and tear down once in the current file
# eg open the db connection execute all the testcases and at last close the db connection
# setup_module - -> only one per file
# setup_class() → one per class
# setup_method() → one per class
# setup_function() → one per class

import pytest

def setup_module(module):
    print("open the db connection")

def teardown_module(module):
    print("close the db connection")

def test_read():
    print("read the db connection")

def test_write():
    print("writing the data to db connection")
def test_update():
    print("update the db connection")

