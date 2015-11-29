import genetic_algorithms_py
import random

iterations = 990
bit_size = 8
target = "10101010"
debug = False

def x_2():
    print '-------------------------'
    print 'Blackbox: x^2'
    black_box = (lambda x: int(x, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)
    print 'Blackbox: deJongSphere'

def dejong():
    print '-------------------------'
    print 'Blackbox: deJongSphere'
    black_box = (lambda x: int(x, 2) + int(target, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)
    print 'Blackbox: deJongSphere'

def rosenbrock():
    print '-------------------------'
    print 'Blackbox: Rosenbrock function'
    a = random.randrange(0, 100)
    b = random.randrange(a, 100)
    black_box = (lambda x: (a + int(x, 2)) ** 2 + b * (
        int(target, 2) - int(x, 2) ** 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)
    print 'Blackbox: Rosenbrock function'

def himmelblau():
    print '-------------------------'
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x: (((int(x, 2) ** 2) + int(target, 2) - 11) ** 2) +
            ((int(x, 2) + (int(target, 2) ** 2) - 7) ** 2))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target)
    print 'Blackbox: Himmelblau function'

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
