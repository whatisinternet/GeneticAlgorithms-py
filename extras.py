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


def ex1():
    print 'Blackbox: deJongSphere function'
    black_box = (lambda a, b, c, d, e, f, g, h, i, j: (abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2) + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2) * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2) + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2) * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2) + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2) * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2) + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2) * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2) + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2) * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2) + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2) * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2))))
    target_fitness = None
    variables = 10
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(10),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "function_name": "ex1"
        }
    genetic_algorithms_py.__init__(params)

ex1()
