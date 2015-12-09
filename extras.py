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


def ex5():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
         + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2) *
        int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2) +
        int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2) *
        int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2) +
        int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2) *
        int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2) +
        int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2) *
        int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2) +
        int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2) *
        int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2) +
        int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2) *
        int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2) +
        int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2) *
        int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2) +
        int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2) *
        int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2) +
        int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2) *
        int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2) +
        int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2) *
        int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2) +
        int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2) *
        int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2) +
        int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2) *
        int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2) +
        int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2) *
        int(n, 2))))

    target_fitness = None
    variables = 14
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
        "function_name": "ex5"
        }
    genetic_algorithms_py.__init__(params)


def ex6():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
         + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2) *
        int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2) +
        int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2) *
        int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2) +
        int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2) *
        int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2) +
        int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2) *
        int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2) +
        int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2) *
        int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2) +
        int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2) *
        int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2) +
        int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2) *
        int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2) +
        int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2) *
        int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2) +
        int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2) *
        int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2) +
        int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2) *
        int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2) +
        int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2) *
        int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2) +
        int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2) *
        int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2) +
        int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2) *
        int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2) +
        int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2) *
        int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2) +
        int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2) *
        int(o, 2))))

    target_fitness = None
    variables = 15
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
        "function_name": "ex6"
        }
    genetic_algorithms_py.__init__(params)


def ex7():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
         + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        *int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
         + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        *int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
         + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        *int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
         + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        *int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
         + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        *int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
         + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        *int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
         + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        *int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
         + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        *int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
         + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        *int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
         + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        *int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
         + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        *int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
         + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        *int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
         + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        *int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
         + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        *int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
         + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        *int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
         + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        *int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
         + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        *int(p, 2) + int(o, 2) * int(p, 2))))

    target_fitness = None
    variables = 16
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
        "function_name": "ex7"
        }
    genetic_algorithms_py.__init__(params)


def ex8():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q:(

        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
         + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        *int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
         + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        *int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
         + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        *int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
         + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        *int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
         + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        *int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
         + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        *int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
         + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        *int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
         + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        *int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
         + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        *int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
         + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        *int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
         + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        *int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
         + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        *int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
         + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        *int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
         + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        *int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
         + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        *int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
         + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        *int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
         + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        *int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
         + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        *int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
         + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        *int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2))))

    target_fitness = None
    variables = 17
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
        "function_name": "ex8"
        }
    genetic_algorithms_py.__init__(params)

def ex9():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r:(

        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
         + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        *int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
         + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        *int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
         + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        *int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
         + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        *int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
         + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        *int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
         + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        *int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
         + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        *int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
         + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        *int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
         + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        *int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
         + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        *int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
         + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        *int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
         + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        *int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
         + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        *int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
         + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        *int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
         + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        *int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
         + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        *int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
         + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        *int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
         + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        *int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
         + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        *int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
         + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2) + int(d, 2)
        *int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2) * int(r, 2)
         + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2) + int(k, 2)
        *int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2) * int(r, 2)
         + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2))))

    target_fitness = None
    variables = 18
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
        "function_name": "ex9"
        }
    genetic_algorithms_py.__init__(params)




def ex10():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s: (


        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2) + int(d, 2)
        * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2) * int(r, 2)
        + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2) + int(k, 2)
        * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2) * int(r, 2)
        + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2) + int(a, 2)
        * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2) * int(s, 2)
        + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2) + int(h, 2)
        * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2) * int(s, 2)
        + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2) + int(o, 2)
        * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2) * int(s, 2))))

    target_fitness = None
    variables = 19
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
        "function_name": "ex10"
        }
    genetic_algorithms_py.__init__(params)


def ex11():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t:(

        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(e, 2) * int(t, 2) + int(f, 2) * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2)
        * int(t, 2) + int(i, 2) * int(t, 2) + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2)
        + int(l, 2) * int(t, 2) + int(m, 2) * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2)
        * int(t, 2) + int(p, 2) * int(t, 2) + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2)
        + int(s, 2) * int(t, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2)
        * int(r, 2) + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2)
        + int(g, 2) * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2)
        * int(r, 2) + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2)
        + int(n, 2) * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2)
        * int(r, 2) + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2)
        + int(d, 2) * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2)
        * int(s, 2) + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2)
        + int(k, 2) * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2)
        * int(s, 2) + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2)
        + int(r, 2) * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2)
        * int(t, 2) + int(d, 2) * int(t, 2))))

    target_fitness = None
    variables = 20
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
        "function_name": "ex11"
        }
    genetic_algorithms_py.__init__(params)


def ex12():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u:(

        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(e, 2) * int(t, 2) + int(f, 2) * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2)
        * int(t, 2) + int(i, 2) * int(t, 2) + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2)
        + int(l, 2) * int(t, 2) + int(m, 2) * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2)
        * int(t, 2) + int(p, 2) * int(t, 2) + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2)
        + int(s, 2) * int(t, 2) + int(a, 2) * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2)
        * int(u, 2) + int(d, 2) * int(u, 2) + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2)
        + int(g, 2) * int(u, 2) + int(h, 2) * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2)
        * int(u, 2) + int(k, 2) * int(u, 2) + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2)
        + int(n, 2) * int(u, 2) + int(o, 2) * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2)
        * int(u, 2) + int(r, 2) * int(u, 2) + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2)
        + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2) + int(d, 2)
        * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2) * int(r, 2)
        + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2) + int(k, 2)
        * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2) * int(r, 2)
        + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2) + int(a, 2)
        * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2) * int(s, 2)
        + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2) + int(h, 2)
        * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2) * int(s, 2)
        + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2) + int(o, 2)
        * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2) * int(s, 2)
        + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2) + int(d, 2)
        * int(t, 2))))

    target_fitness = None
    variables = 21
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
        "function_name": "ex12"
        }
    genetic_algorithms_py.__init__(params)


def ex13():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v:(


        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)+
        int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)*
        int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)+
        int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)*
        int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)+
        int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)*
        int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)+
        int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)*
        int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)+
        int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)*
        int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)+
        int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)*
        int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)+
        int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)*
        int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)+
        int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)*
        int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)+
        int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)*
        int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)+
        int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)*
        int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)+
        int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)*
        int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)+
        int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)*
        int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)+
        int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)*
        int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)+
        int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)*
        int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)+
        int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)*
        int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)+
        int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)*
        int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)+
        int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)*
        int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)+
        int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)*
        int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)+
        int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)*
        int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)+
        int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)*
        int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)+
        int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)*
        int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)+
        int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)*
        int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)+
        int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)*
        int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)+
        int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)*
        int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)+
        int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)*
        int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)+
        int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)*
        int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)+
        int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)*
        int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)+
        int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)*
        int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)+
        int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)*
        int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)+
        int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)*
        int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)+
        int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)*
        int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)+
        int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)*
        int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)+
        int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)*
        int(v, 2))))

    target_fitness = None
    variables = 22
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
         "function_name": "ex13"
         }
    genetic_algorithms_py.__init__(params)

def ex14():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w:(

        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)
        * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)
        + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)
        * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)
        + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)
        * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)
        + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)
        * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)
        + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)
        * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)
        + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)
        * int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)
        + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)
        * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)
        + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)
        * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)
        + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)
        * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)
        + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)
        * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)
        + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)
        * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)
        + int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)
        * int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)
        + int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)
        * int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)
        + int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)
        * int(v, 2) + int(a, 2) * int(w, 2) + int(b, 2) * int(w, 2) + int(c, 2) * int(w, 2)
        + int(d, 2) * int(w, 2) + int(e, 2) * int(w, 2) + int(f, 2) * int(w, 2) + int(g, 2)
        * int(w, 2) + int(h, 2) * int(w, 2) + int(i, 2) * int(w, 2) + int(j, 2) * int(w, 2)
        + int(k, 2) * int(w, 2) + int(l, 2) * int(w, 2) + int(m, 2) * int(w, 2) + int(n, 2)
        * int(w, 2) + int(o, 2) * int(w, 2) + int(p, 2) * int(w, 2) + int(q, 2) * int(w, 2)
        + int(r, 2) * int(w, 2) + int(s, 2) * int(w, 2) + int(t, 2) * int(w, 2) + int(u, 2)
        * int(w, 2) + int(v, 2) * int(w, 2))))

    target_fitness = None
    variables = 23
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
        "function_name": "ex14"
        }
    genetic_algorithms_py.__init__(params)


def ex15():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)
        * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)
        + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)
        * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)
        + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)
        * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)
        + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)
        * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)
        + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)
        * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)
        + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)
        * int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)
        + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)
        * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)
        + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)
        * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)
        + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)
        * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)
        + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)
        * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)
        + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)
        * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)
        + int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)
        * int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)
        + int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)
        * int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)
        + int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)
        * int(v, 2) + int(a, 2) * int(w, 2) + int(b, 2) * int(w, 2) + int(c, 2) * int(w, 2)
        + int(d, 2) * int(w, 2) + int(e, 2) * int(w, 2) + int(f, 2) * int(w, 2) + int(g, 2)
        * int(w, 2) + int(h, 2) * int(w, 2) + int(i, 2) * int(w, 2) + int(j, 2) * int(w, 2)
        + int(k, 2) * int(w, 2) + int(l, 2) * int(w, 2) + int(m, 2) * int(w, 2) + int(n, 2)
        * int(w, 2) + int(o, 2) * int(w, 2) + int(p, 2) * int(w, 2) + int(q, 2) * int(w, 2)
        + int(r, 2) * int(w, 2) + int(s, 2) * int(w, 2) + int(t, 2) * int(w, 2) + int(u, 2)
        * int(w, 2) + int(v, 2) * int(w, 2) + int(a, 2) * int(x, 2) + int(b, 2) * int(x, 2)
        + int(c, 2) * int(x, 2) + int(d, 2) * int(x, 2) + int(e, 2) * int(x, 2) + int(f, 2)
        * int(x, 2) + int(g, 2) * int(x, 2) + int(h, 2) * int(x, 2) + int(i, 2) * int(x, 2)
        + int(j, 2) * int(x, 2) + int(k, 2) * int(x, 2) + int(l, 2) * int(x, 2) + int(m, 2)
        * int(x, 2) + int(n, 2) * int(x, 2) + int(o, 2) * int(x, 2) + int(p, 2) * int(x, 2)
        + int(q, 2) * int(x, 2) + int(r, 2) * int(x, 2) + int(s, 2) * int(x, 2) + int(t, 2)
        * int(x, 2) + int(u, 2) * int(x, 2) + int(v, 2) * int(x, 2) + int(w, 2) * int(x, 2))))

    target_fitness = None
    variables = 24
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
        "function_name": "ex15"
        }
    genetic_algorithms_py.__init__(params)

def ex16():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)
        * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)
        + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)
        * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)
        + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)
        * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)
        + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)
        * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)
        + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)
        * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)
        + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)
        * int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)
        + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)
        * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)
        + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)
        * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)
        + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)
        * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)
        + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)
        * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)
        + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)
        * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)
        + int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)
        * int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)
        + int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)
        * int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)
        + int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)
        * int(v, 2) + int(a, 2) * int(w, 2) + int(b, 2) * int(w, 2) + int(c, 2) * int(w, 2)
        + int(d, 2) * int(w, 2) + int(e, 2) * int(w, 2) + int(f, 2) * int(w, 2) + int(g, 2)
        * int(w, 2) + int(h, 2) * int(w, 2) + int(i, 2) * int(w, 2) + int(j, 2) * int(w, 2)
        + int(k, 2) * int(w, 2) + int(l, 2) * int(w, 2) + int(m, 2) * int(w, 2) + int(n, 2)
        * int(w, 2) + int(o, 2) * int(w, 2) + int(p, 2) * int(w, 2) + int(q, 2) * int(w, 2)
        + int(r, 2) * int(w, 2) + int(s, 2) * int(w, 2) + int(t, 2) * int(w, 2) + int(u, 2)
        * int(w, 2) + int(v, 2) * int(w, 2) + int(a, 2) * int(x, 2) + int(b, 2) * int(x, 2)
        + int(c, 2) * int(x, 2) + int(d, 2) * int(x, 2) + int(e, 2) * int(x, 2) + int(f, 2)
        * int(x, 2) + int(g, 2) * int(x, 2) + int(h, 2) * int(x, 2) + int(i, 2) * int(x, 2)
        + int(j, 2) * int(x, 2) + int(k, 2) * int(x, 2) + int(l, 2) * int(x, 2) + int(m, 2)
        * int(x, 2) + int(n, 2) * int(x, 2) + int(o, 2) * int(x, 2) + int(p, 2) * int(x, 2)
        + int(q, 2) * int(x, 2) + int(r, 2) * int(x, 2) + int(s, 2) * int(x, 2) + int(t, 2)
        * int(x, 2) + int(u, 2) * int(x, 2) + int(v, 2) * int(x, 2) + int(w, 2) * int(x, 2)
        + int(a, 2) * int(y, 2) + int(b, 2) * int(y, 2) + int(c, 2) * int(y, 2) + int(d, 2)
        * int(y, 2) + int(e, 2) * int(y, 2) + int(f, 2) * int(y, 2) + int(g, 2) * int(y, 2)
        + int(h, 2) * int(y, 2) + int(i, 2) * int(y, 2) + int(j, 2) * int(y, 2) + int(k, 2)
        * int(y, 2) + int(l, 2) * int(y, 2) + int(m, 2) * int(y, 2) + int(n, 2) * int(y, 2)
        + int(o, 2) * int(y, 2) + int(p, 2) * int(y, 2) + int(q, 2) * int(y, 2) + int(r, 2)
        * int(y, 2) + int(s, 2) * int(y, 2) + int(t, 2) * int(y, 2) + int(u, 2) * int(y, 2)
        + int(v, 2) * int(y, 2) + int(w, 2) * int(y, 2) + int(x, 2) * int(y, 2))))

    target_fitness = None
    variables = 25
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
        "function_name": "ex16"
        }
    genetic_algorithms_py.__init__(params)


def ex17():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)+
        int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)*
        int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)
        * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)
        + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)
        * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)
        + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)
        * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)
        + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)
        * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)
        + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)
        * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)
        + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)
        * int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)
        + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)
        * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)
        + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)
        * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)
        + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)
        * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)
        + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)
        * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)
        + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)
        * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)
        + int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)
        * int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)
        + int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)
        * int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)
        + int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)
        * int(v, 2) + int(a, 2) * int(w, 2) + int(b, 2) * int(w, 2) + int(c, 2) * int(w, 2)
        + int(d, 2) * int(w, 2) + int(e, 2) * int(w, 2) + int(f, 2) * int(w, 2) + int(g, 2)
        * int(w, 2) + int(h, 2) * int(w, 2) + int(i, 2) * int(w, 2) + int(j, 2) * int(w, 2)
        + int(k, 2) * int(w, 2) + int(l, 2) * int(w, 2) + int(m, 2) * int(w, 2) + int(n, 2)
        * int(w, 2) + int(o, 2) * int(w, 2) + int(p, 2) * int(w, 2) + int(q, 2) * int(w, 2)
        + int(r, 2) * int(w, 2) + int(s, 2) * int(w, 2) + int(t, 2) * int(w, 2) + int(u, 2)
        * int(w, 2) + int(v, 2) * int(w, 2) + int(a, 2) * int(x, 2) + int(b, 2) * int(x, 2)
        + int(c, 2) * int(x, 2) + int(d, 2) * int(x, 2) + int(e, 2) * int(x, 2) + int(f, 2)
        * int(x, 2) + int(g, 2) * int(x, 2) + int(h, 2) * int(x, 2) + int(i, 2) * int(x, 2)
        + int(j, 2) * int(x, 2) + int(k, 2) * int(x, 2) + int(l, 2) * int(x, 2) + int(m, 2)
        * int(x, 2) + int(n, 2) * int(x, 2) + int(o, 2) * int(x, 2) + int(p, 2) * int(x, 2)
        + int(q, 2) * int(x, 2) + int(r, 2) * int(x, 2) + int(s, 2) * int(x, 2) + int(t, 2)
        * int(x, 2) + int(u, 2) * int(x, 2) + int(v, 2) * int(x, 2) + int(w, 2) * int(x, 2)
        + int(a, 2) * int(y, 2) + int(b, 2) * int(y, 2) + int(c, 2) * int(y, 2) + int(d, 2)
        * int(y, 2) + int(e, 2) * int(y, 2) + int(f, 2) * int(y, 2) + int(g, 2) * int(y, 2)
        + int(h, 2) * int(y, 2) + int(i, 2) * int(y, 2) + int(j, 2) * int(y, 2) + int(k, 2)
        * int(y, 2) + int(l, 2) * int(y, 2) + int(m, 2) * int(y, 2) + int(n, 2) * int(y, 2)
        + int(o, 2) * int(y, 2) + int(p, 2) * int(y, 2) + int(q, 2) * int(y, 2) + int(r, 2)
        * int(y, 2) + int(s, 2) * int(y, 2) + int(t, 2) * int(y, 2) + int(u, 2) * int(y, 2)
        + int(v, 2) * int(y, 2) + int(w, 2) * int(y, 2) + int(x, 2) * int(y, 2) + int(a, 2)
        * int(z, 2) + int(b, 2) * int(z, 2) + int(c, 2) * int(z, 2) + int(d, 2) * int(z, 2)
        + int(e, 2) * int(z, 2) + int(f, 2) * int(z, 2) + int(g, 2) * int(z, 2) + int(h, 2)
        * int(z, 2) + int(i, 2) * int(z, 2) + int(j, 2) * int(z, 2) + int(k, 2) * int(z, 2)
        + int(l, 2) * int(z, 2) + int(m, 2) * int(z, 2) + int(n, 2) * int(z, 2) + int(o, 2)
        * int(z, 2) + int(p, 2) * int(z, 2) + int(q, 2) * int(z, 2) + int(r, 2) * int(z, 2)
        + int(s, 2) * int(z, 2) + int(t, 2) * int(z, 2) + int(u, 2) * int(z, 2) + int(v, 2)
        * int(z, 2) + int(w, 2) * int(z, 2) + int(x, 2) * int(z, 2) + int(y, 2) * int(z, 2))))

    target_fitness = None
    variables = 26
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
        "function_name": "ex17"
        }
    genetic_algorithms_py.__init__(params)

def ex18():
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a2:(
        abs(int(a, 2) * int(b, 2) + int(a, 2) * int(c, 2) + int(a, 2) * int(d, 2)
        + int(a, 2) * int(e, 2) + int(a, 2) * int(f, 2) + int(a, 2) * int(g, 2) + int(a, 2)
        * int(h, 2) + int(a, 2) * int(i, 2) + int(a, 2) * int(j, 2) + int(b, 2) * int(c, 2)
        + int(b, 2) * int(d, 2) + int(b, 2) * int(e, 2) + int(b, 2) * int(f, 2) + int(b, 2)
        * int(g, 2) + int(b, 2) * int(h, 2) + int(b, 2) * int(i, 2) + int(b, 2) * int(j, 2)
        + int(c, 2) * int(d, 2) + int(c, 2) * int(e, 2) + int(c, 2) * int(f, 2) + int(c, 2)
        * int(g, 2) + int(c, 2) * int(h, 2) + int(c, 2) * int(i, 2) + int(c, 2) * int(j, 2)
        + int(d, 2) * int(e, 2) + int(d, 2) * int(f, 2) + int(d, 2) * int(g, 2) + int(d, 2)
        * int(h, 2) + int(d, 2) * int(i, 2) + int(d, 2) * int(j, 2) + int(e, 2) * int(f, 2)
        + int(e, 2) * int(g, 2) + int(e, 2) * int(h, 2) + int(e, 2) * int(i, 2) + int(e, 2)
        * int(j, 2) + int(f, 2) * int(g, 2) + int(f, 2) * int(h, 2) + int(f, 2) * int(i, 2)
        + int(f, 2) * int(j, 2) + int(g, 2) * int(h, 2) + int(g, 2) * int(i, 2) + int(g, 2)
        * int(j, 2) + int(h, 2) * int(i, 2) + int(h, 2) * int(j, 2) + int(i, 2) * int(j, 2)
        + int(a, 2) * int(k, 2) + int(b, 2) * int(k, 2) + int(c, 2) * int(k, 2) + int(d, 2)
        * int(k, 2) + int(e, 2) * int(k, 2) + int(f, 2) * int(k, 2) + int(g, 2) * int(k, 2)
        + int(h, 2) * int(k, 2) + int(i, 2) * int(k, 2) + int(j, 2) * int(k, 2) + int(a, 2)
        * int(l, 2) + int(b, 2) * int(l, 2) + int(c, 2) * int(l, 2) + int(d, 2) * int(l, 2)
        + int(e, 2) * int(l, 2) + int(f, 2) * int(l, 2) + int(g, 2) * int(l, 2) + int(h, 2)
        * int(l, 2) + int(i, 2) * int(l, 2) + int(j, 2) * int(l, 2) + int(k, 2) * int(l, 2)
        + int(a, 2) * int(m, 2) + int(b, 2) * int(m, 2) + int(c, 2) * int(m, 2) + int(d, 2)
        * int(m, 2) + int(e, 2) * int(m, 2) + int(f, 2) * int(m, 2) + int(g, 2) * int(m, 2)
        + int(h, 2) * int(m, 2) + int(i, 2) * int(m, 2) + int(j, 2) * int(m, 2) + int(k, 2)
        * int(m, 2) + int(l, 2) * int(m, 2) + int(a, 2) * int(n, 2) + int(b, 2) * int(n, 2)
        + int(c, 2) * int(n, 2) + int(d, 2) * int(n, 2) + int(e, 2) * int(n, 2) + int(f, 2)
        * int(n, 2) + int(g, 2) * int(n, 2) + int(h, 2) * int(n, 2) + int(i, 2) * int(n, 2)
        + int(j, 2) * int(n, 2) + int(k, 2) * int(n, 2) + int(l, 2) * int(n, 2) + int(m, 2)
        * int(n, 2) + int(a, 2) * int(o, 2) + int(b, 2) * int(o, 2) + int(c, 2) * int(o, 2)
        + int(d, 2) * int(o, 2) + int(e, 2) * int(o, 2) + int(f, 2) * int(o, 2) + int(g, 2)
        * int(o, 2) + int(h, 2) * int(o, 2) + int(i, 2) * int(o, 2) + int(j, 2) * int(o, 2)
        + int(k, 2) * int(o, 2) + int(l, 2) * int(o, 2) + int(m, 2) * int(o, 2) + int(n, 2)
        * int(o, 2) + int(a, 2) * int(p, 2) + int(b, 2) * int(p, 2) + int(c, 2) * int(p, 2)
        + int(d, 2) * int(p, 2) + int(e, 2) * int(p, 2) + int(f, 2) * int(p, 2) + int(g, 2)
        * int(p, 2) + int(h, 2) * int(p, 2) + int(i, 2) * int(p, 2) + int(j, 2) * int(p, 2)
        + int(k, 2) * int(p, 2) + int(l, 2) * int(p, 2) + int(m, 2) * int(p, 2) + int(n, 2)
        * int(p, 2) + int(o, 2) * int(p, 2) + int(a, 2) * int(q, 2) + int(b, 2) * int(q, 2)
        + int(c, 2) * int(q, 2) + int(d, 2) * int(q, 2) + int(e, 2) * int(q, 2) + int(f, 2)
        * int(q, 2) + int(g, 2) * int(q, 2) + int(h, 2) * int(q, 2) + int(i, 2) * int(q, 2)
        + int(j, 2) * int(q, 2) + int(k, 2) * int(q, 2) + int(l, 2) * int(q, 2) + int(m, 2)
        * int(q, 2) + int(n, 2) * int(q, 2) + int(o, 2) * int(q, 2) + int(p, 2) * int(q, 2)
        + int(c, 2) * int(v, 2) + int(d, 2) * int(v, 2) + int(e, 2) * int(t, 2) + int(f, 2)
        * int(t, 2) + int(g, 2) * int(t, 2) + int(h, 2) * int(t, 2) + int(i, 2) * int(t, 2)
        + int(j, 2) * int(t, 2) + int(k, 2) * int(t, 2) + int(l, 2) * int(t, 2) + int(m, 2)
        * int(t, 2) + int(n, 2) * int(t, 2) + int(o, 2) * int(t, 2) + int(p, 2) * int(t, 2)
        + int(q, 2) * int(t, 2) + int(r, 2) * int(t, 2) + int(s, 2) * int(t, 2) + int(a, 2)
        * int(u, 2) + int(b, 2) * int(u, 2) + int(c, 2) * int(u, 2) + int(d, 2) * int(u, 2)
        + int(e, 2) * int(u, 2) + int(f, 2) * int(u, 2) + int(g, 2) * int(u, 2) + int(h, 2)
        * int(u, 2) + int(i, 2) * int(u, 2) + int(j, 2) * int(u, 2) + int(k, 2) * int(u, 2)
        + int(l, 2) * int(u, 2) + int(m, 2) * int(u, 2) + int(n, 2) * int(u, 2) + int(o, 2)
        * int(u, 2) + int(p, 2) * int(u, 2) + int(q, 2) * int(u, 2) + int(r, 2) * int(u, 2)
        + int(s, 2) * int(u, 2) + int(t, 2) * int(u, 2) + int(a, 2) * int(v, 2) + int(b, 2)
        * int(v, 2) + int(a, 2) * int(r, 2) + int(b, 2) * int(r, 2) + int(c, 2) * int(r, 2)
        + int(d, 2) * int(r, 2) + int(e, 2) * int(r, 2) + int(f, 2) * int(r, 2) + int(g, 2)
        * int(r, 2) + int(h, 2) * int(r, 2) + int(i, 2) * int(r, 2) + int(j, 2) * int(r, 2)
        + int(k, 2) * int(r, 2) + int(l, 2) * int(r, 2) + int(m, 2) * int(r, 2) + int(n, 2)
        * int(r, 2) + int(o, 2) * int(r, 2) + int(p, 2) * int(r, 2) + int(q, 2) * int(r, 2)
        + int(a, 2) * int(s, 2) + int(b, 2) * int(s, 2) + int(c, 2) * int(s, 2) + int(d, 2)
        * int(s, 2) + int(e, 2) * int(s, 2) + int(f, 2) * int(s, 2) + int(g, 2) * int(s, 2)
        + int(h, 2) * int(s, 2) + int(i, 2) * int(s, 2) + int(j, 2) * int(s, 2) + int(k, 2)
        * int(s, 2) + int(l, 2) * int(s, 2) + int(m, 2) * int(s, 2) + int(n, 2) * int(s, 2)
        + int(o, 2) * int(s, 2) + int(p, 2) * int(s, 2) + int(q, 2) * int(s, 2) + int(r, 2)
        * int(s, 2) + int(a, 2) * int(t, 2) + int(b, 2) * int(t, 2) + int(c, 2) * int(t, 2)
        + int(d, 2) * int(t, 2) + int(e, 2) * int(v, 2) + int(f, 2) * int(v, 2) + int(g, 2)
        * int(v, 2) + int(h, 2) * int(v, 2) + int(i, 2) * int(v, 2) + int(j, 2) * int(v, 2)
        + int(k, 2) * int(v, 2) + int(l, 2) * int(v, 2) + int(m, 2) * int(v, 2) + int(n, 2)
        * int(v, 2) + int(o, 2) * int(v, 2) + int(p, 2) * int(v, 2) + int(q, 2) * int(v, 2)
        + int(r, 2) * int(v, 2) + int(s, 2) * int(v, 2) + int(t, 2) * int(v, 2) + int(u, 2)
        * int(v, 2) + int(a, 2) * int(w, 2) + int(b, 2) * int(w, 2) + int(c, 2) * int(w, 2)
        + int(d, 2) * int(w, 2) + int(e, 2) * int(w, 2) + int(f, 2) * int(w, 2) + int(g, 2)
        * int(w, 2) + int(h, 2) * int(w, 2) + int(i, 2) * int(w, 2) + int(j, 2) * int(w, 2)
        + int(k, 2) * int(w, 2) + int(l, 2) * int(w, 2) + int(m, 2) * int(w, 2) + int(n, 2)
        * int(w, 2) + int(o, 2) * int(w, 2) + int(p, 2) * int(w, 2) + int(q, 2) * int(w, 2)
        + int(r, 2) * int(w, 2) + int(s, 2) * int(w, 2) + int(t, 2) * int(w, 2) + int(u, 2)
        * int(w, 2) + int(v, 2) * int(w, 2) + int(a, 2) * int(x, 2) + int(b, 2) * int(x, 2)
        + int(c, 2) * int(x, 2) + int(d, 2) * int(x, 2) + int(e, 2) * int(x, 2) + int(f, 2)
        * int(x, 2) + int(g, 2) * int(x, 2) + int(h, 2) * int(x, 2) + int(i, 2) * int(x, 2)
        + int(j, 2) * int(x, 2) + int(k, 2) * int(x, 2) + int(l, 2) * int(x, 2) + int(m, 2)
        * int(x, 2) + int(n, 2) * int(x, 2) + int(o, 2) * int(x, 2) + int(p, 2) * int(x, 2)
        + int(q, 2) * int(x, 2) + int(r, 2) * int(x, 2) + int(s, 2) * int(x, 2) + int(t, 2)
        * int(x, 2) + int(u, 2) * int(x, 2) + int(v, 2) * int(x, 2) + int(w, 2) * int(x, 2)
        + int(a, 2) * int(y, 2) + int(b, 2) * int(y, 2) + int(c, 2) * int(y, 2) + int(d, 2)
        * int(y, 2) + int(e, 2) * int(y, 2) + int(f, 2) * int(y, 2) + int(g, 2) * int(y, 2)
        + int(h, 2) * int(y, 2) + int(i, 2) * int(y, 2) + int(j, 2) * int(y, 2) + int(k, 2)
        * int(y, 2) + int(l, 2) * int(y, 2) + int(m, 2) * int(y, 2) + int(n, 2) * int(y, 2)
        + int(o, 2) * int(y, 2) + int(p, 2) * int(y, 2) + int(q, 2) * int(y, 2) + int(r, 2)
        * int(y, 2) + int(s, 2) * int(y, 2) + int(t, 2) * int(y, 2) + int(u, 2) * int(y, 2)
        + int(v, 2) * int(y, 2) + int(w, 2) * int(y, 2) + int(x, 2) * int(y, 2) + int(a, 2)
        * int(z, 2) + int(b, 2) * int(z, 2) + int(c, 2) * int(z, 2) + int(d, 2) * int(z, 2)
        + int(e, 2) * int(z, 2) + int(f, 2) * int(z, 2) + int(g, 2) * int(z, 2) + int(h, 2)
        * int(z, 2) + int(i, 2) * int(z, 2) + int(j, 2) * int(z, 2) + int(k, 2) * int(z, 2)
        + int(l, 2) * int(z, 2) + int(m, 2) * int(z, 2) + int(n, 2) * int(z, 2) + int(o, 2)
        * int(z, 2) + int(p, 2) * int(z, 2) + int(q, 2) * int(z, 2) + int(r, 2) * int(z, 2)
        + int(s, 2) * int(z, 2) + int(t, 2) * int(z, 2) + int(u, 2) * int(z, 2) + int(v, 2)
        * int(z, 2) + int(w, 2) * int(z, 2) + int(x, 2) * int(z, 2) + int(y, 2) * int(z, 2)
        + int(a, 2) * int(a2, 2) + int(b, 2) * int(a2, 2) + int(c, 2) * int(a2, 2) +
        int(d, 2) * int(a2, 2) + int(e, 2) * int(a2, 2) + int(f, 2) * int(a2, 2) +
        int(g, 2) * int(a2, 2) + int(h, 2) * int(a2, 2) + int(i, 2) * int(a2, 2) +
        int(j, 2) * int(a2, 2) + int(k, 2) * int(a2, 2) + int(l, 2) * int(a2, 2) +
        int(m, 2) * int(a2, 2) + int(n, 2) * int(a2, 2) + int(o, 2) * int(a2, 2) +
        int(p, 2) * int(a2, 2) + int(q, 2) * int(a2, 2) + int(r, 2) * int(a2, 2) +
        int(s, 2) * int(a2, 2) + int(t, 2) * int(a2, 2) + int(u, 2) * int(a2, 2) +
        int(v, 2) * int(a2, 2) + int(w, 2) * int(a2, 2) + int(x, 2) * int(a2, 2) +
        int(y, 2) * int(a2, 2) + int(z, 2) * int(a2, 2))))

    target_fitness = None
    variables = 27
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
        "function_name": "ex18"
        }
    genetic_algorithms_py.__init__(params)

print "EX1"
ex1()
print "EX5"
ex5()
print "EX6"
ex6()
print "EX7"
ex7()
print "EX8"
ex8()
print "EX9"
ex9()
print "EX10"
ex10()
print "EX11"
ex11()
print "EX12"
ex12()
print "EX13"
ex13()
print "EX14"
ex14()
print "EX15"
ex15()
print "EX16"
ex16()
print "EX17"
ex17()
print "EX18"
ex18()
