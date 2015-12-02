import genetic_algorithms_py

black_box = (lambda x, y: int(y, 2) + int(x, 2) ** 2)


'''
Init values:
    black_box
    iterations
    constraint_range
    pool_size
    mutation_probability
    crossover_rate
    target fitness
    number_of_variables in black box
'''


def test_it_should_get_an_initialization_vector():
    assert isinstance(genetic_algorithms_py.__init__(black_box, 1, range(8),
                                                     2, 0.0, 0.0, 2, 8, None),
                      list)
