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

params = {
    'objective_function': black_box,
    'iterations': 1,
    'mutation_probability': 0.0,
    "crossover_rate": 0.0,
    "constraint_range": range(8),
    "number_of_variables": 2,
    "carry_over": 2,
    "pool_size": 2,
    "target": None,
    "function_name": None
    }

def test_it_should_get_an_initialization_vector():
    assert isinstance(genetic_algorithms_py.__init__(params), list)
