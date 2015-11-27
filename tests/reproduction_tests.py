from nose.tools import *
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction

def test_it_should_return_an_array_of_string():
    seeding_pool = seeding.pool(8)
    asserted_pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool, '11111111')
    assert len(asserted_pool) == 8
