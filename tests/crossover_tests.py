from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction
from genetic_algorithms_py import crossover


black_box = (lambda x, y: int(y) + int(x) ** 2)

def test_it_should_return_an_array_of_size_2():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    asserted_pool = crossover.crossover(pool)
    assert len(asserted_pool) == 2


def test_it_should_return_an_array_of_strings():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    asserted_pool = crossover.crossover(pool)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)


# Private tests
def test__pair_up_should_return_1_tuple():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    mated_seeds = crossover._pair_up(pool)
    assert len(mated_seeds) == 1


def test__pair_up_should_return_n_tuples():
    seeding_pool = seeding.pool(2, 8)
    pool = reproduction.reproduce(black_box, seeding_pool, 2)
    mated_seeds = crossover._pair_up(pool)
    for mated in mated_seeds:
        assert isinstance(mated, tuple)
