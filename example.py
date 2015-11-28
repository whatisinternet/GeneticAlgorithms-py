import genetic_algorithms_py
import random

iterations = 100
bit_size = 8
target = "10101010"
debug = True

def x_2():
    print '-------------------------'
    print 'Blackbox: x^2'
    black_box = (lambda x: int(x, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)

def dejong():
    print '-------------------------'
    print 'Blackbox: deJongSphere'
    black_box = (lambda vector: reduce(lambda x, y: int(y, 2) + int(x) ** 2, vector))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)

def rosenbrock():
    print '-------------------------'
    print 'Blackbox: Rosenbrock function'
    a = random.randrange(0, 100)
    b = random.randrange(a, 100)
    black_box = (lambda vector: reduce(lambda x, y: (a + int(y, 2)) ** 2 + b * (
        int(x) - int(y, 2) ** 2) ** 2, vector))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)

def himmelblau():
    print '-------------------------'
    print 'Blackbox: Himmelblau function'
    black_box = (lambda vector: reduce(
        lambda x, y:
            (((int(x) ** 2) + int(y, 2) - 11) ** 2) +
            ((int(x) + (int(y, 2) ** 2) - 7) ** 2),
            vector))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)

x_2()
if debug:
    raw_input()
dejong()
if debug:
    raw_input()
rosenbrock()
if debug:
    raw_input()
himmelblau()
if debug:
    raw_input()
