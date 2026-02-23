#fixture dependency - the second fixture will work only when first fixture

import pytest
def test(fixture_b):
    assert fixture_b == "Data from A" + "Data from B"
#fixture_b  automatically receives the value from fixture_a

#hirachy of execution - fixture_a -- fixture_b -- test