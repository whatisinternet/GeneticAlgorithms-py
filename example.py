import genetic_algorithms_py
import random

def _is_debugging():
    f = open('./debug','r')
    debug = f.readline()
    if debug  == "True\n":
        return True
    else:
        return False

#------------------------------
iterations = 990 #Max is 990
bit_size = 8
target = "10101010" # MUST be set and equal to bit size
debug = _is_debugging()

def x_2():
    print '-------------------------'
    print 'Blackbox: x^2'
    black_box = (lambda x: int(x, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target, "X^2")
    print 'Blackbox: deJongSphere'

def dejong():
    print '-------------------------'
    print 'Blackbox: deJongSphere'
    black_box = (lambda x: int(x, 2) + int(target, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target, "deJong Sphere")
    print 'Blackbox: deJongSphere'

def rosenbrock():
    print '-------------------------'
    print 'Blackbox: Rosenbrock function'
    a = random.randrange(0, 100)
    b = random.randrange(a, 100)
    black_box = (lambda x: (a + int(x, 2)) ** 2 + b * (
        int(target, 2) - int(x, 2) ** 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target, "Rosenbrock Function")
    print 'Blackbox: Rosenbrock function'

def himmelblau():
    print '-------------------------'
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x: (((int(x, 2) ** 2) + int(target, 2) - 11) ** 2) +
            ((int(x, 2) + (int(target, 2) ** 2) - 7) ** 2))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, target, "Himmelblau Function")
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

