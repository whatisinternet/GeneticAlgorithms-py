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


def ex1(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j: (abs(a * b + a * c + a * d + a * e + a * f + a * g + a * h + a * i + a * j + b * c + b * d + b * e + b * f + b * g + b * h + b * i + b * j + c * d + c * e + c * f + c * g + c * h + c * i + c * j + d * e + d * f + d * g + d * h + d * i + d * j + e * f + e * g + e * h + e * i + e * j + f * g + f * h + f * i + f * j + g * h + g * i + g * j + h * i + h * j + i * j)))
    target_fitness = None
    variables = 10
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex1"
        }
    genetic_algorithms_py.__init__(params)


def ex2(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k:(

  abs(a * b + a * c + a * d
  + a * e + a * f + a * g + a * h
  + a * i + a * j + b * c + b * d
  + b * e + b * f + b * g + b * h
  + b * i + b * j + c * d + c * e
  + c * f + c * g + c * h + c * i
  + c * j + d * e + d * f + d * g
  + d * h + d * i + d * j + e * f
  + e * g + e * h + e * i + e * j
  + f * g + f * h + f * i + f * j
  + g * h + g * i + g * j + h * i
  + h * j + i * j + a * k + b * k
  + c * k + d * k + e * k + f * k
  + g * k + h * k + i * k + j * k)))

    target_fitness = None
    variables = 11
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex2"
        }
    genetic_algorithms_py.__init__(params)


def ex3(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l:(

  abs(a * b + a * c + a * d
  + a * e + a * f + a * g + a * h
  + a * i + a * j + b * c + b * d
  + b * e + b * f + b * g + b * h
  + b * i + b * j + c * d + c * e
  + c * f + c * g + c * h + c * i
  + c * j + d * e + d * f + d * g
  + d * h + d * i + d * j + e * f
  + e * g + e * h + e * i + e * j
  + f * g + f * h + f * i + f * j
  + g * h + g * i + g * j + h * i
  + h * j + i * j + a * k + b * k
  + c * k + d * k + e * k + f * k
  + g * k + h * k + i * k + j * k
  + a * l + b * l + c * l + d * l
  + e * l + f * l + g * l + h * l
  + i * l + j * l + k * l)))

    target_fitness = None
    variables = 12
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex3"
        }
    genetic_algorithms_py.__init__(params)


def ex4(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m:(

  abs(a * b + a * c + a * d
  + a * e + a * f + a * g + a * h
  + a * i + a * j + b * c + b * d
  + b * e + b * f + b * g + b * h
  + b * i + b * j + c * d + c * e
  + c * f + c * g + c * h + c * i
  + c * j + d * e + d * f + d * g
  + d * h + d * i + d * j + e * f
  + e * g + e * h + e * i + e * j
  + f * g + f * h + f * i + f * j
  + g * h + g * i + g * j + h * i
  + h * j + i * j + a * k + b * k
  + c * k + d * k + e * k + f * k
  + g * k + h * k + i * k + j * k
  + a * l + b * l + c * l + d * l
  + e * l + f * l + g * l + h * l
  + i * l + j * l + k * l + a * m
  + b * m + c * m + d * m + e * m
  + f * m + g * m + h * m + i * m
  + j * m + k * m + l * m)))

    target_fitness = None
    variables = 13
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex4"
        }
    genetic_algorithms_py.__init__(params)


def ex5(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n:(
        abs(a * b + a * c + a * d
         + a * e + a * f + a * g + a *
        h + a * i + a * j + b * c +
        b * d + b * e + b * f + b *
        g + b * h + b * i + b * j +
        c * d + c * e + c * f + c *
        g + c * h + c * i + c * j +
        d * e + d * f + d * g + d *
        h + d * i + d * j + e * f +
        e * g + e * h + e * i + e *
        j + f * g + f * h + f * i +
        f * j + g * h + g * i + g *
        j + h * i + h * j + i * j +
        a * k + b * k + c * k + d *
        k + e * k + f * k + g * k +
        h * k + i * k + j * k + a *
        l + b * l + c * l + d * l +
        e * l + f * l + g * l + h *
        l + i * l + j * l + k * l +
        a * m + b * m + c * m + d *
        m + e * m + f * m + g * m +
        h * m + i * m + j * m + k *
        m + l * m + a * n + b * n +
        c * n + d * n + e * n + f *
        n + g * n + h * n + i * n +
        j * n + k * n + l * n + m *
        n)))

    target_fitness = None
    variables = 14
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex5"
        }
    genetic_algorithms_py.__init__(params)


def ex6(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o:(
        abs(a * b + a * c + a * d
         + a * e + a * f + a * g + a *
        h + a * i + a * j + b * c +
        b * d + b * e + b * f + b *
        g + b * h + b * i + b * j +
        c * d + c * e + c * f + c *
        g + c * h + c * i + c * j +
        d * e + d * f + d * g + d *
        h + d * i + d * j + e * f +
        e * g + e * h + e * i + e *
        j + f * g + f * h + f * i +
        f * j + g * h + g * i + g *
        j + h * i + h * j + i * j +
        a * k + b * k + c * k + d *
        k + e * k + f * k + g * k +
        h * k + i * k + j * k + a *
        l + b * l + c * l + d * l +
        e * l + f * l + g * l + h *
        l + i * l + j * l + k * l +
        a * m + b * m + c * m + d *
        m + e * m + f * m + g * m +
        h * m + i * m + j * m + k *
        m + l * m + a * n + b * n +
        c * n + d * n + e * n + f *
        n + g * n + h * n + i * n +
        j * n + k * n + l * n + m *
        n + a * o + b * o + c * o +
        d * o + e * o + f * o + g *
        o + h * o + i * o + j * o +
        k * o + l * o + m * o + n *
        o)))

    target_fitness = None
    variables = 15
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex6"
        }
    genetic_algorithms_py.__init__(params)


def ex7(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p:(
        abs(a * b + a * c + a * d
         + a * e + a * f + a * g + a
        *h + a * i + a * j + b * c
         + b * d + b * e + b * f + b
        *g + b * h + b * i + b * j
         + c * d + c * e + c * f + c
        *g + c * h + c * i + c * j
         + d * e + d * f + d * g + d
        *h + d * i + d * j + e * f
         + e * g + e * h + e * i + e
        *j + f * g + f * h + f * i
         + f * j + g * h + g * i + g
        *j + h * i + h * j + i * j
         + a * k + b * k + c * k + d
        *k + e * k + f * k + g * k
         + h * k + i * k + j * k + a
        *l + b * l + c * l + d * l
         + e * l + f * l + g * l + h
        *l + i * l + j * l + k * l
         + a * m + b * m + c * m + d
        *m + e * m + f * m + g * m
         + h * m + i * m + j * m + k
        *m + l * m + a * n + b * n
         + c * n + d * n + e * n + f
        *n + g * n + h * n + i * n
         + j * n + k * n + l * n + m
        *n + a * o + b * o + c * o
         + d * o + e * o + f * o + g
        *o + h * o + i * o + j * o
         + k * o + l * o + m * o + n
        *o + a * p + b * p + c * p
         + d * p + e * p + f * p + g
        *p + h * p + i * p + j * p
         + k * p + l * p + m * p + n
        *p + o * p)))

    target_fitness = None
    variables = 16
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex7"
        }
    genetic_algorithms_py.__init__(params)


def ex8(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q:(

        abs(a * b + a * c + a * d
         + a * e + a * f + a * g + a
        *h + a * i + a * j + b * c
         + b * d + b * e + b * f + b
        *g + b * h + b * i + b * j
         + c * d + c * e + c * f + c
        *g + c * h + c * i + c * j
         + d * e + d * f + d * g + d
        *h + d * i + d * j + e * f
         + e * g + e * h + e * i + e
        *j + f * g + f * h + f * i
         + f * j + g * h + g * i + g
        *j + h * i + h * j + i * j
         + a * k + b * k + c * k + d
        *k + e * k + f * k + g * k
         + h * k + i * k + j * k + a
        *l + b * l + c * l + d * l
         + e * l + f * l + g * l + h
        *l + i * l + j * l + k * l
         + a * m + b * m + c * m + d
        *m + e * m + f * m + g * m
         + h * m + i * m + j * m + k
        *m + l * m + a * n + b * n
         + c * n + d * n + e * n + f
        *n + g * n + h * n + i * n
         + j * n + k * n + l * n + m
        *n + a * o + b * o + c * o
         + d * o + e * o + f * o + g
        *o + h * o + i * o + j * o
         + k * o + l * o + m * o + n
        *o + a * p + b * p + c * p
         + d * p + e * p + f * p + g
        *p + h * p + i * p + j * p
         + k * p + l * p + m * p + n
        *p + o * p + a * q + b * q
         + c * q + d * q + e * q + f
        *q + g * q + h * q + i * q
         + j * q + k * q + l * q + m
        *q + n * q + o * q + p * q)))

    target_fitness = None
    variables = 17
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex8"
        }
    genetic_algorithms_py.__init__(params)

def ex9(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r:(

        abs(a * b + a * c + a * d
         + a * e + a * f + a * g + a
        *h + a * i + a * j + b * c
         + b * d + b * e + b * f + b
        *g + b * h + b * i + b * j
         + c * d + c * e + c * f + c
        *g + c * h + c * i + c * j
         + d * e + d * f + d * g + d
        *h + d * i + d * j + e * f
         + e * g + e * h + e * i + e
        *j + f * g + f * h + f * i
         + f * j + g * h + g * i + g
        *j + h * i + h * j + i * j
         + a * k + b * k + c * k + d
        *k + e * k + f * k + g * k
         + h * k + i * k + j * k + a
        *l + b * l + c * l + d * l
         + e * l + f * l + g * l + h
        *l + i * l + j * l + k * l
         + a * m + b * m + c * m + d
        *m + e * m + f * m + g * m
         + h * m + i * m + j * m + k
        *m + l * m + a * n + b * n
         + c * n + d * n + e * n + f
        *n + g * n + h * n + i * n
         + j * n + k * n + l * n + m
        *n + a * o + b * o + c * o
         + d * o + e * o + f * o + g
        *o + h * o + i * o + j * o
         + k * o + l * o + m * o + n
        *o + a * p + b * p + c * p
         + d * p + e * p + f * p + g
        *p + h * p + i * p + j * p
         + k * p + l * p + m * p + n
        *p + o * p + a * q + b * q
         + c * q + d * q + e * q + f
        *q + g * q + h * q + i * q
         + j * q + k * q + l * q + m
        *q + n * q + o * q + p * q
         + a * r + b * r + c * r + d
        *r + e * r + f * r + g * r
         + h * r + i * r + j * r + k
        *r + l * r + m * r + n * r
         + o * r + p * r + q * r)))

    target_fitness = None
    variables = 18
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex9"
        }
    genetic_algorithms_py.__init__(params)




def ex10(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s: (


        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + a * r + b * r + c * r + d
        * r + e * r + f * r + g * r
        + h * r + i * r + j * r + k
        * r + l * r + m * r + n * r
        + o * r + p * r + q * r + a
        * s + b * s + c * s + d * s
        + e * s + f * s + g * s + h
        * s + i * s + j * s + k * s
        + l * s + m * s + n * s + o
        * s + p * s + q * s + r * s)))

    target_fitness = None
    variables = 19
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex10"
        }
    genetic_algorithms_py.__init__(params)


def ex11(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t:(

        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + e * t + f * t + g * t + h
        * t + i * t + j * t + k * t
        + l * t + m * t + n * t + o
        * t + p * t + q * t + r * t
        + s * t + a * r + b * r + c
        * r + d * r + e * r + f * r
        + g * r + h * r + i * r + j
        * r + k * r + l * r + m * r
        + n * r + o * r + p * r + q
        * r + a * s + b * s + c * s
        + d * s + e * s + f * s + g
        * s + h * s + i * s + j * s
        + k * s + l * s + m * s + n
        * s + o * s + p * s + q * s
        + r * s + a * t + b * t + c
        * t + d * t)))

    target_fitness = None
    variables = 20
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex11"
        }
    genetic_algorithms_py.__init__(params)


def ex12(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u:(

        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + e * t + f * t + g * t + h
        * t + i * t + j * t + k * t
        + l * t + m * t + n * t + o
        * t + p * t + q * t + r * t
        + s * t + a * u + b * u + c
        * u + d * u + e * u + f * u
        + g * u + h * u + i * u + j
        * u + k * u + l * u + m * u
        + n * u + o * u + p * u + q
        * u + r * u + s * u + t * u
        + a * r + b * r + c * r + d
        * r + e * r + f * r + g * r
        + h * r + i * r + j * r + k
        * r + l * r + m * r + n * r
        + o * r + p * r + q * r + a
        * s + b * s + c * s + d * s
        + e * s + f * s + g * s + h
        * s + i * s + j * s + k * s
        + l * s + m * s + n * s + o
        * s + p * s + q * s + r * s
        + a * t + b * t + c * t + d
        * t)))

    target_fitness = None
    variables = 21
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex12"
        }
    genetic_algorithms_py.__init__(params)


def ex13(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v:(


        abs(a * b + a * c + a * d+
        a * e + a * f + a * g + a*
        h + a * i + a * j + b * c+
        b * d + b * e + b * f + b*
        g + b * h + b * i + b * j+
        c * d + c * e + c * f + c*
        g + c * h + c * i + c * j+
        d * e + d * f + d * g + d*
        h + d * i + d * j + e * f+
        e * g + e * h + e * i + e*
        j + f * g + f * h + f * i+
        f * j + g * h + g * i + g*
        j + h * i + h * j + i * j+
        a * k + b * k + c * k + d*
        k + e * k + f * k + g * k+
        h * k + i * k + j * k + a*
        l + b * l + c * l + d * l+
        e * l + f * l + g * l + h*
        l + i * l + j * l + k * l+
        a * m + b * m + c * m + d*
        m + e * m + f * m + g * m+
        h * m + i * m + j * m + k*
        m + l * m + a * n + b * n+
        c * n + d * n + e * n + f*
        n + g * n + h * n + i * n+
        j * n + k * n + l * n + m*
        n + a * o + b * o + c * o+
        d * o + e * o + f * o + g*
        o + h * o + i * o + j * o+
        k * o + l * o + m * o + n*
        o + a * p + b * p + c * p+
        d * p + e * p + f * p + g*
        p + h * p + i * p + j * p+
        k * p + l * p + m * p + n*
        p + o * p + a * q + b * q+
        c * q + d * q + e * q + f*
        q + g * q + h * q + i * q+
        j * q + k * q + l * q + m*
        q + n * q + o * q + p * q+
        c * v + d * v + e * t + f*
        t + g * t + h * t + i * t+
        j * t + k * t + l * t + m*
        t + n * t + o * t + p * t+
        q * t + r * t + s * t + a*
        u + b * u + c * u + d * u+
        e * u + f * u + g * u + h*
        u + i * u + j * u + k * u+
        l * u + m * u + n * u + o*
        u + p * u + q * u + r * u+
        s * u + t * u + a * v + b*
        v + a * r + b * r + c * r+
        d * r + e * r + f * r + g*
        r + h * r + i * r + j * r+
        k * r + l * r + m * r + n*
        r + o * r + p * r + q * r+
        a * s + b * s + c * s + d*
        s + e * s + f * s + g * s+
        h * s + i * s + j * s + k*
        s + l * s + m * s + n * s+
        o * s + p * s + q * s + r*
        s + a * t + b * t + c * t+
        d * t + e * v + f * v + g*
        v + h * v + i * v + j * v+
        k * v + l * v + m * v + n*
        v + o * v + p * v + q * v+
        r * v + s * v + t * v + u*
        v)))

    target_fitness = None
    variables = 22
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex13"
        }
    genetic_algorithms_py.__init__(params)

def ex14(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w:(

        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + c * v + d * v + e * t + f
        * t + g * t + h * t + i * t
        + j * t + k * t + l * t + m
        * t + n * t + o * t + p * t
        + q * t + r * t + s * t + a
        * u + b * u + c * u + d * u
        + e * u + f * u + g * u + h
        * u + i * u + j * u + k * u
        + l * u + m * u + n * u + o
        * u + p * u + q * u + r * u
        + s * u + t * u + a * v + b
        * v + a * r + b * r + c * r
        + d * r + e * r + f * r + g
        * r + h * r + i * r + j * r
        + k * r + l * r + m * r + n
        * r + o * r + p * r + q * r
        + a * s + b * s + c * s + d
        * s + e * s + f * s + g * s
        + h * s + i * s + j * s + k
        * s + l * s + m * s + n * s
        + o * s + p * s + q * s + r
        * s + a * t + b * t + c * t
        + d * t + e * v + f * v + g
        * v + h * v + i * v + j * v
        + k * v + l * v + m * v + n
        * v + o * v + p * v + q * v
        + r * v + s * v + t * v + u
        * v + a * w + b * w + c * w
        + d * w + e * w + f * w + g
        * w + h * w + i * w + j * w
        + k * w + l * w + m * w + n
        * w + o * w + p * w + q * w
        + r * w + s * w + t * w + u
        * w + v * w)))

    target_fitness = None
    variables = 23
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex14"
        }
    genetic_algorithms_py.__init__(params)


def ex15(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x:(
        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + c * v + d * v + e * t + f
        * t + g * t + h * t + i * t
        + j * t + k * t + l * t + m
        * t + n * t + o * t + p * t
        + q * t + r * t + s * t + a
        * u + b * u + c * u + d * u
        + e * u + f * u + g * u + h
        * u + i * u + j * u + k * u
        + l * u + m * u + n * u + o
        * u + p * u + q * u + r * u
        + s * u + t * u + a * v + b
        * v + a * r + b * r + c * r
        + d * r + e * r + f * r + g
        * r + h * r + i * r + j * r
        + k * r + l * r + m * r + n
        * r + o * r + p * r + q * r
        + a * s + b * s + c * s + d
        * s + e * s + f * s + g * s
        + h * s + i * s + j * s + k
        * s + l * s + m * s + n * s
        + o * s + p * s + q * s + r
        * s + a * t + b * t + c * t
        + d * t + e * v + f * v + g
        * v + h * v + i * v + j * v
        + k * v + l * v + m * v + n
        * v + o * v + p * v + q * v
        + r * v + s * v + t * v + u
        * v + a * w + b * w + c * w
        + d * w + e * w + f * w + g
        * w + h * w + i * w + j * w
        + k * w + l * w + m * w + n
        * w + o * w + p * w + q * w
        + r * w + s * w + t * w + u
        * w + v * w + a * x + b * x
        + c * x + d * x + e * x + f
        * x + g * x + h * x + i * x
        + j * x + k * x + l * x + m
        * x + n * x + o * x + p * x
        + q * x + r * x + s * x + t
        * x + u * x + v * x + w * x)))

    target_fitness = None
    variables = 24
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex15"
        }
    genetic_algorithms_py.__init__(params)

def ex16(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y:(
        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + c * v + d * v + e * t + f
        * t + g * t + h * t + i * t
        + j * t + k * t + l * t + m
        * t + n * t + o * t + p * t
        + q * t + r * t + s * t + a
        * u + b * u + c * u + d * u
        + e * u + f * u + g * u + h
        * u + i * u + j * u + k * u
        + l * u + m * u + n * u + o
        * u + p * u + q * u + r * u
        + s * u + t * u + a * v + b
        * v + a * r + b * r + c * r
        + d * r + e * r + f * r + g
        * r + h * r + i * r + j * r
        + k * r + l * r + m * r + n
        * r + o * r + p * r + q * r
        + a * s + b * s + c * s + d
        * s + e * s + f * s + g * s
        + h * s + i * s + j * s + k
        * s + l * s + m * s + n * s
        + o * s + p * s + q * s + r
        * s + a * t + b * t + c * t
        + d * t + e * v + f * v + g
        * v + h * v + i * v + j * v
        + k * v + l * v + m * v + n
        * v + o * v + p * v + q * v
        + r * v + s * v + t * v + u
        * v + a * w + b * w + c * w
        + d * w + e * w + f * w + g
        * w + h * w + i * w + j * w
        + k * w + l * w + m * w + n
        * w + o * w + p * w + q * w
        + r * w + s * w + t * w + u
        * w + v * w + a * x + b * x
        + c * x + d * x + e * x + f
        * x + g * x + h * x + i * x
        + j * x + k * x + l * x + m
        * x + n * x + o * x + p * x
        + q * x + r * x + s * x + t
        * x + u * x + v * x + w * x
        + a * y + b * y + c * y + d
        * y + e * y + f * y + g * y
        + h * y + i * y + j * y + k
        * y + l * y + m * y + n * y
        + o * y + p * y + q * y + r
        * y + s * y + t * y + u * y
        + v * y + w * y + x * y)))

    target_fitness = None
    variables = 25
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex16"
        }
    genetic_algorithms_py.__init__(params)


def ex17(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z:(
        abs(a * b + a * c + a * d+
        a * e + a * f + a * g + a*
        h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + c * v + d * v + e * t + f
        * t + g * t + h * t + i * t
        + j * t + k * t + l * t + m
        * t + n * t + o * t + p * t
        + q * t + r * t + s * t + a
        * u + b * u + c * u + d * u
        + e * u + f * u + g * u + h
        * u + i * u + j * u + k * u
        + l * u + m * u + n * u + o
        * u + p * u + q * u + r * u
        + s * u + t * u + a * v + b
        * v + a * r + b * r + c * r
        + d * r + e * r + f * r + g
        * r + h * r + i * r + j * r
        + k * r + l * r + m * r + n
        * r + o * r + p * r + q * r
        + a * s + b * s + c * s + d
        * s + e * s + f * s + g * s
        + h * s + i * s + j * s + k
        * s + l * s + m * s + n * s
        + o * s + p * s + q * s + r
        * s + a * t + b * t + c * t
        + d * t + e * v + f * v + g
        * v + h * v + i * v + j * v
        + k * v + l * v + m * v + n
        * v + o * v + p * v + q * v
        + r * v + s * v + t * v + u
        * v + a * w + b * w + c * w
        + d * w + e * w + f * w + g
        * w + h * w + i * w + j * w
        + k * w + l * w + m * w + n
        * w + o * w + p * w + q * w
        + r * w + s * w + t * w + u
        * w + v * w + a * x + b * x
        + c * x + d * x + e * x + f
        * x + g * x + h * x + i * x
        + j * x + k * x + l * x + m
        * x + n * x + o * x + p * x
        + q * x + r * x + s * x + t
        * x + u * x + v * x + w * x
        + a * y + b * y + c * y + d
        * y + e * y + f * y + g * y
        + h * y + i * y + j * y + k
        * y + l * y + m * y + n * y
        + o * y + p * y + q * y + r
        * y + s * y + t * y + u * y
        + v * y + w * y + x * y + a
        * z + b * z + c * z + d * z
        + e * z + f * z + g * z + h
        * z + i * z + j * z + k * z
        + l * z + m * z + n * z + o
        * z + p * z + q * z + r * z
        + s * z + t * z + u * z + v
        * z + w * z + x * z + y * z)))

    target_fitness = None
    variables = 26
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex17"
        }
    genetic_algorithms_py.__init__(params)

def ex18(maximize):
    black_box = (lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a2:(
        abs(a * b + a * c + a * d
        + a * e + a * f + a * g + a
        * h + a * i + a * j + b * c
        + b * d + b * e + b * f + b
        * g + b * h + b * i + b * j
        + c * d + c * e + c * f + c
        * g + c * h + c * i + c * j
        + d * e + d * f + d * g + d
        * h + d * i + d * j + e * f
        + e * g + e * h + e * i + e
        * j + f * g + f * h + f * i
        + f * j + g * h + g * i + g
        * j + h * i + h * j + i * j
        + a * k + b * k + c * k + d
        * k + e * k + f * k + g * k
        + h * k + i * k + j * k + a
        * l + b * l + c * l + d * l
        + e * l + f * l + g * l + h
        * l + i * l + j * l + k * l
        + a * m + b * m + c * m + d
        * m + e * m + f * m + g * m
        + h * m + i * m + j * m + k
        * m + l * m + a * n + b * n
        + c * n + d * n + e * n + f
        * n + g * n + h * n + i * n
        + j * n + k * n + l * n + m
        * n + a * o + b * o + c * o
        + d * o + e * o + f * o + g
        * o + h * o + i * o + j * o
        + k * o + l * o + m * o + n
        * o + a * p + b * p + c * p
        + d * p + e * p + f * p + g
        * p + h * p + i * p + j * p
        + k * p + l * p + m * p + n
        * p + o * p + a * q + b * q
        + c * q + d * q + e * q + f
        * q + g * q + h * q + i * q
        + j * q + k * q + l * q + m
        * q + n * q + o * q + p * q
        + c * v + d * v + e * t + f
        * t + g * t + h * t + i * t
        + j * t + k * t + l * t + m
        * t + n * t + o * t + p * t
        + q * t + r * t + s * t + a
        * u + b * u + c * u + d * u
        + e * u + f * u + g * u + h
        * u + i * u + j * u + k * u
        + l * u + m * u + n * u + o
        * u + p * u + q * u + r * u
        + s * u + t * u + a * v + b
        * v + a * r + b * r + c * r
        + d * r + e * r + f * r + g
        * r + h * r + i * r + j * r
        + k * r + l * r + m * r + n
        * r + o * r + p * r + q * r
        + a * s + b * s + c * s + d
        * s + e * s + f * s + g * s
        + h * s + i * s + j * s + k
        * s + l * s + m * s + n * s
        + o * s + p * s + q * s + r
        * s + a * t + b * t + c * t
        + d * t + e * v + f * v + g
        * v + h * v + i * v + j * v
        + k * v + l * v + m * v + n
        * v + o * v + p * v + q * v
        + r * v + s * v + t * v + u
        * v + a * w + b * w + c * w
        + d * w + e * w + f * w + g
        * w + h * w + i * w + j * w
        + k * w + l * w + m * w + n
        * w + o * w + p * w + q * w
        + r * w + s * w + t * w + u
        * w + v * w + a * x + b * x
        + c * x + d * x + e * x + f
        * x + g * x + h * x + i * x
        + j * x + k * x + l * x + m
        * x + n * x + o * x + p * x
        + q * x + r * x + s * x + t
        * x + u * x + v * x + w * x
        + a * y + b * y + c * y + d
        * y + e * y + f * y + g * y
        + h * y + i * y + j * y + k
        * y + l * y + m * y + n * y
        + o * y + p * y + q * y + r
        * y + s * y + t * y + u * y
        + v * y + w * y + x * y + a
        * z + b * z + c * z + d * z
        + e * z + f * z + g * z + h
        * z + i * z + j * z + k * z
        + l * z + m * z + n * z + o
        * z + p * z + q * z + r * z
        + s * z + t * z + u * z + v
        * z + w * z + x * z + y * z
        + a * a2 + b * a2 + c * a2 +
        d * a2 + e * a2 + f * a2 +
        g * a2 + h * a2 + i * a2 +
        j * a2 + k * a2 + l * a2 +
        m * a2 + n * a2 + o * a2 +
        p * a2 + q * a2 + r * a2 +
        s * a2 + t * a2 + u * a2 +
        v * a2 + w * a2 + x * a2 +
        y * a2 + z * a2)))

    target_fitness = None
    variables = 27
    carry_over = 64
    params = {
        'objective_function': black_box,
        'iterations': iterations,
        'mutation_probability': mutation_probability,
        "crossover_rate": crossover_rate,
        "constraint_range": range(1000000),
        "number_of_variables": variables,
        "carry_over": carry_over,
        "pool_size": initial_pool,
        "target": target_fitness,
        "max": maximize,
        "function_name": "ex18"
        }
    genetic_algorithms_py.__init__(params)

print "Maximize------------------------------------------\n\n\n"
print "EX1"
ex1(True)
print "EX2"
ex2(True)
print "EX3"
ex3(True)
print "EX4"
ex4(True)
print "EX5"
ex5(True)
print "EX6"
ex6(True)
print "EX7"
ex7(True)
print "EX8"
ex8(True)
print "EX9"
ex9(True)
print "EX10"
ex10(True)
print "EX11"
ex11(True)
print "EX12"
ex12(True)
print "EX13"
ex13(True)
print "EX14"
ex14(True)
print "EX15"
ex15(True)
print "EX16"
ex16(True)
print "EX17"
ex17(True)
print "EX18"
ex18(True)

print "\n\n\n\nMinimize------------------------------------------\n\n\n"
print "EX1"
ex1(False)
print "EX2"
ex2(False)
print "EX3"
ex3(False)
print "EX4"
ex4(False)
print "EX5"
ex5(False)
print "EX6"
ex6(False)
print "EX7"
ex7(False)
print "EX8"
ex8(False)
print "EX9"
ex9(False)
print "EX10"
ex10(False)
print "EX11"
ex11(False)
print "EX12"
ex12(False)
print "EX13"
ex13(False)
print "EX14"
ex14(False)
print "EX15"
ex15(False)
print "EX16"
ex16(False)
print "EX17"
ex17(False)
print "EX18"
ex18(False)
