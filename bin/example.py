import genetic_algorithms_py


def _is_debugging():
    f = open('./debug', 'r')
    debug = f.readline()
    if debug is "True\n":
        return True
    else:
        return False

iterations = 100
debug = _is_debugging()
initial_pool = 200
mutation_probability = 0.001
crossover_rate = 0.7
carry_over = initial_pool / 2


def dejong(maximize):
    print 'Blackbox: deJongSphere function'
    black_box = (lambda x, y: (reduce(
        (lambda r, q: q + (int(x, 2) ** 2)), range(int(y, 2)), 0)))
    target_fitness = None
    variables = 2
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(165),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "deJong Sphere maximized: {a}".format(a=maximize)
        }
    genetic_algorithms_py.__init__(params)


def rosenbrock(maximize):
    print 'Blackbox: Rosenbrock function'
    reducer_size = 100
    black_box = (lambda x, y, z: (reduce(
        (lambda p, q: q + (100 * ((int(x, 2) - (int(y, 2) ** 2) ) ** 2) + (1 - int(y, 2)) ** 2)), range(int(z, 2)), 0)))
    target_fitness = None
    variables = 3
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(0,500),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "Rosenbrock Function maximized: {a}".format(a=maximize)
        }
    genetic_algorithms_py.__init__(params)


def himmelblau(maximize):
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x, y: (((int(x, 2) ** 2) + int(y, 2) - 11) ** 2) +
                 ((int(x, 2) + (int(y,2) ** 2) - 7) ** 2))
    target_fitness = None
    variables = 2
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(-500,500),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "Himmelblau Function maximized: {a}".format(a=maximize)
        }
    genetic_algorithms_py.__init__(params)

dejong(True)
rosenbrock(True)
himmelblau(True)

dejong(False)
rosenbrock(False)
himmelblau(False)
