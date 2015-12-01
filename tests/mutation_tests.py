from genetic_algorithms_py import mutation
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover

black_box = (lambda x, y: int(y) + int(x) ** 2)

def test_it_should_return_a_mutated_string():
    mutated_string = mutation.mutate("101")
    assert len(mutated_string) == 3


def test_it_should_mutate_a_pool_returning_2_strings():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    crossed_over = crossover.crossover(pool)
    asserted_pool = mutation.mutate_pool(crossed_over)
    assert len(asserted_pool) == 2


def test_it_should_mutate_a_pool_returning_n_strings():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    crossed_over = crossover.crossover(pool)
    asserted_pool = mutation.mutate_pool(crossed_over)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)
