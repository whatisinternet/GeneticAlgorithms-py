from nose.tools import *
import itertools
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover

def test_it_should_return_an_array_of_size_2():
    seeding_pool = seeding.pool(2)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    asserted_pool = crossover.crossover(pool)
    print asserted_pool
    assert len(asserted_pool) == 2

def test_it_should_return_an_array_of_strings():
    seeding_pool = seeding.pool(8)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    asserted_pool = crossover.crossover(pool)
    for asserted in asserted_pool:
        assert isinstance( asserted, str )

# Private tests
def test__pair_up_should_return_1_tuple():
    seeding_pool = seeding.pool(2)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    mated_seeds = crossover._pair_up(pool)
    assert len(mated_seeds) == 1

def test__pair_up_should_return_n_tuples():
    seeding_pool = seeding.pool(8)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    mated_seeds = crossover._pair_up(pool)
    for mated in mated_seeds:
        assert isinstance(mated, tuple)
