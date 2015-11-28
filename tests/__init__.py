from nose.tools import *
import genetic_algorithms_py

def test_it_should_get_an_initialization_vector():
    assert isinstance(
            genetic_algorithms_py.__init__(),
            basestring)
