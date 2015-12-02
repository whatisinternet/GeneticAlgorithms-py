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
initial_pool = 20
mutation_probability = 0.001

'''
Init values:
    black_box
    iterations
    constraint_range
    pool_size
    mutation_probability
    target fitness
    number_of_variables in black box
'''

def dejong():
    print 'Blackbox: deJongSphere function'
    black_box = (lambda x, y: (reduce(
        (lambda r, q: q + (int(x, 2) ** 2)), range(int(y, 2)), 0)))
    target_fitness = None
    variables = 2
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(65),
                                   initial_pool,
                                   mutation_probability,
                                   variables,
                                   target_fitness,
                                   "deJong Sphere")


def rosenbrock():
    print 'Blackbox: Rosenbrock function'
    reducer_size = 100
    black_box = (lambda x, y, z: (reduce(
        (lambda p, q: q + (100 * ((int(x, 2) - (int(y, 2) ** 2) ) ** 2) + (1 - int(y, 2)) ** 2)), range(int(z, 2)), 0)))
    target_fitness = None
    variables = 3
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(0,500),
                                   initial_pool,
                                   mutation_probability,
                                   variables,
                                   target_fitness,
                                   "Rosenbrock Function")


def himmelblau():
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x, y: (((int(x, 2) ** 2) + int(y, 2) - 11) ** 2) +
                 ((int(x, 2) + (int(y,2) ** 2) - 7) ** 2))
    target_fitness = None
    variables = 2
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(-500,500),
                                   initial_pool,
                                   mutation_probability,
                                   variables,
                                   target_fitness,
                                   "Himmelblau Function")


dejong()
if debug:
    raw_input()
rosenbrock()
if debug:
    raw_input()
himmelblau()
if debug:
    raw_input()
