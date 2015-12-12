import genetic_algorithms_py

black_box = (lambda x, y: y + x ** 2)
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
    'max': True,
    "function_name": None
    }


def test_it_should_return():
    assert isinstance(genetic_algorithms_py.__init__(params), list)
