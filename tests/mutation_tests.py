from genetic_algorithms_py import mutation
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover

black_box = (lambda x, y: int(y) + int(x) ** 2)
mutation_probability = 0.5
crossover_rate = 0.5
params = {'objective_function': black_box,
          'pool': seeding.pool(8, range(255), 2),
          'pool_size': 8,
          'number_of_variables': 2,
          'carry_over': 2}


def test_it_should_return_a_mutated_string():
    mutated_string = mutation.mutate("101", mutation_probability)
    assert len(mutated_string) == 3


def test_it_should_mutate_a_pool_returning_2_strings():
    pool = reproduction.reproduce(params)
    crossed_over = crossover.crossover(pool, crossover_rate)
    asserted_pool = mutation.mutate_pool(crossed_over, mutation_probability)
    assert len(asserted_pool) >= 2


def test_it_should_mutate_a_pool_returning_n_strings():
    pool = reproduction.reproduce(params)
    crossed_over = crossover.crossover(pool, crossover_rate)
    asserted_pool = mutation.mutate_pool(crossed_over, mutation_probability)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)
