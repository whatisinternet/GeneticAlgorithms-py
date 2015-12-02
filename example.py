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
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(65),
                                   initial_pool,
                                   mutation_probability,
                                   2,
                                   111512,
                                   "deJong Sphere")


def rosenbrock():
    print 'Blackbox: Rosenbrock function'
    reducer_size = 100
    black_box = (lambda x, y, z: (reduce(
        (lambda p, q: q + (100 * ((int(x, 2) - (int(y, 2) ** 2) ) ** 2) + (1 - int(y, 2)) ** 2)), range(int(z, 2)), 0)))
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(0,500),
                                   initial_pool,
                                   mutation_probability,
                                   3,
                                   0,
                                   "Rosenbrock Function")


def himmelblau():
    print 'Blackbox: Himmelblau function'
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, 2,
                                   mutation_probability, initial_pool,
                                   "Himmelblau Function")


dejong()
if debug:
    raw_input()
rosenbrock()
if debug:
    raw_input()
# himmelblau()
# if debug:
#     raw_input()
