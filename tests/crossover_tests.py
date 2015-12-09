from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover


black_box = (lambda x, y: int(y) + int(x) ** 2)
params = {'objective_function': black_box,
          'pool': seeding.pool(8, range(255), 2),
          'pool_size': 8,
          'number_of_variables': 2,
          'carry_over': 2,
          'max': True,
          'crossover_rate': 0.7}

def test_it_should_return_an_array_of_size_2():
    params['pool'] = reproduction.reproduce(params)
    asserted_pool = crossover.crossover(params)
    assert len(asserted_pool) >= 2


def test_it_should_return_an_array_of_strings():
    params['pool'] = reproduction.reproduce(params)
    asserted_pool = crossover.crossover(params)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)


# Private tests
def test__pair_up_should_return_1_tuple():
    pool = reproduction.reproduce(params)
    mated_seeds = crossover._pair_up(pool)
    assert len(mated_seeds) >= 1


def test__pair_up_should_return_n_tuples():
    pool = reproduction.reproduce(params)
    mated_seeds = crossover._pair_up(pool)
    for mated in mated_seeds:
        assert isinstance(mated, tuple)
