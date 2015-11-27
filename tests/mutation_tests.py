from nose.tools import *
from genetic_algorithms_py import mutation
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover

def test_it_should_return_a_mutated_string():
    mutated_string = mutation.mutate("101")
    assert len(mutated_string) == 3

def test_it_should_mutate_a_pool_returning_n_strings():
    seeding_pool = seeding.pool(2)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    crossed_over = crossover.crossover(pool)
    asserted_pool = mutation.mutate_pool(crossed_over)
    assert len(asserted_pool) == 2

def test_it_should_mutate_a_pool_returning_n_strings():
    seeding_pool = seeding.pool(2)
    pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    crossed_over = crossover.crossover(pool)
    asserted_pool = mutation.mutate_pool(crossed_over)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)
