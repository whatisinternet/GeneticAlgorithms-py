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
iterations = 900
bit_size = 8
debug = _is_debugging()


def dejong():
    print 'Blackbox: deJongSphere function'
    black_box = (lambda x, y: int(x, 2) + int(y, 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, 2, "deJong Sphere")


def rosenbrock():
    print 'Blackbox: Rosenbrock function'
    black_box = (lambda a, b, c, x: (int(a, 2) + int(x, 2)) ** 2 + int(b, 2) * (
        int(c, 2) - int(x, 2) ** 2) ** 2)
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, 4, "Rosenbrock Function")


def himmelblau():
    print 'Blackbox: Himmelblau function'
    black_box = (lambda x, y: (((int(x, 2) ** 2) + int(y, 2) - 11) ** 2) +
            ((int(x, 2) + (int(y, 2) ** 2) - 7) ** 2))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, 2, "Himmelblau Function")


def production():
    print 'Blackbox: Production function'
    black_box = (lambda a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s: int(a, 2) +
                 int(b, 2) +  int(f, 2) +  int(j, 2) +  int(n, 2) +  int(q, 2) +
                 int(c, 2) +  int(g, 2) +  int(k, 2) +  int(o, 2) +  int(r, 2) +
                 int(d, 2) +  int(h, 2) +  int(l, 2) +  int(p, 2) +  int(s, 2) +
                 int(e, 2) +  int(i, 2) +  int(m, 2))
    genetic_algorithms_py.__init__(black_box, iterations, bit_size, 19, "Productuon Function")


dejong()
if debug:
    raw_input()
rosenbrock()
if debug:
    raw_input()
himmelblau()
if debug:
    raw_input()
production()
if debug:
    raw_input()
