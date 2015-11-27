from nose.tools import *
from genetic_algorithms_py import random_vector

def test_it_should_return_a_string():
    assert isinstance(
            random_vector.initialization_vector(),
            basestring)

def test_it_should_only_return_a_string_of_1_and_0():
    asserted_string =  random_vector.initialization_vector()
    for i in asserted_string:
        assert (i == "1" or i == "0")
