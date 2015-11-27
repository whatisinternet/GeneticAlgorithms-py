from nose.tools import *
from genetic_algorithms_py import seeding
from genetic_algorithms_py import random_vector

def test_it_should_return_an_array_of_string():
    initial_vector = random_vector.initialization_vector()
    asserted_pool = seeding.pool(initial_vector, 8)
    assert len(asserted_pool) == 8

def test_it_should_only_return_an_array_of_strings_containing_only_1_and_0():
    initial_vector = random_vector.initialization_vector()
    asserted_pool = seeding.pool(initial_vector, 8)
    for asserted_string in asserted_pool:
        for i in asserted_string:
            assert (i == "1" or i == "0")
