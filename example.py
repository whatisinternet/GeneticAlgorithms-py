import genetic_algorithms_py


def _is_debugging():
    f = open('./debug', 'r')
    debug = f.readline()
    if debug is "True\n":
        return True
    else:
        return False

iterations = 1000000000
debug = _is_debugging()
initial_pool = 200
mutation_probability = 0.001
crossover_rate = 0.7
carry_over = initial_pool / 2


'''
Init values:
    black_box
    iterations
    constraint_range
    pool_size
    mutation_probability
    crossover_rate
    carry_over
    target fitness
    number_of_variables in black box
'''

def dejong():
    print 'Blackbox: deJongSphere function'
    black_box = (lambda x, y: (reduce(
        (lambda r, q: q + (int(x, 2) ** 2)), range(int(y, 2)), 0)))
    target_fitness = None
    variables = 2
    carry_over = 64
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(1165),
                                   initial_pool,
                                   mutation_probability,
                                   crossover_rate,
                                   variables,
                                   carry_over,
                                   target_fitness,
                                   "deJong Sphere")


def rosenbrock():
    print 'Blackbox: Rosenbrock function'
    reducer_size = 100
    black_box = (lambda x, y, z: (reduce(
        (lambda p, q: q + (100 * ((int(x, 2) - (int(y, 2) ** 2) ) ** 2) + (1 - int(y, 2)) ** 2)), range(int(z, 2)), 0)))
    target_fitness = None
    variables = 3
    carry_over = 64
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(0,500),
                                   initial_pool,
                                   mutation_probability,
                                   crossover_rate,
                                   variables,
                                   carry_over,
                                   target_fitness,
                                   "Rosenbrock Function")


def himmelblau():
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x, y: (((int(x, 2) ** 2) + int(y, 2) - 11) ** 2) +
                 ((int(x, 2) + (int(y,2) ** 2) - 7) ** 2))
    target_fitness = None
    variables = 2
    carry_over = 64
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(-500,500),
                                   initial_pool,
                                   mutation_probability,
                                   crossover_rate,
                                   variables,
                                   carry_over,
                                   target_fitness,
                                   "Himmelblau Function")

def alphabet_soup():
    print 'Blackbox: Alphabet soup function'

    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o,
                 p, q, r, s, t, u, v, w, x, y, z: int(a, 2) + int(b, 2) +
                 int(c, 2) - int(d, 2) * int(e, 2) + int(f, 2) -
                 int(g, 2) - int(h, 2) * int(i, 2) + int(j, 2) -
                 int(k, 2) - int(l, 2) * int(m, 2) + int(n, 2) -
                 int(o, 2) - int(p, 2) * int(q, 2) + int(s, 2) -
                 int(t, 2) - int(u, 2) * int(v, 2) + int(w, 2) -
                 int(x, 2) - int(y, 2) * int(z, 2))
    target_fitness = None
    variables = 26
    carry_over = 64
    genetic_algorithms_py.__init__(black_box,
                                   iterations,
                                   range(-500,500),
                                   initial_pool,
                                   mutation_probability,
                                   crossover_rate,
                                   variables,
                                   carry_over,
                                   target_fitness,
                                   "alphabet Function")

dejong()
# rosenbrock()
# himmelblau()
# alphabet_soup()
