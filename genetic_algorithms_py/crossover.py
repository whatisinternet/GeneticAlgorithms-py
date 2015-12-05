import random


def crossover(params):
    pool = params['pool']
    rate = params['crossover_rate']

    if _is_crossable(rate):
        crossed = map(lambda x: _cross(x), _pair_up(pool))
        return sum(crossed, [])
    else:
        return pool


# Private ----
def _cross(seedling):
    #cross binary strings at random index 0 to string length-1. The first half comes
    #from the first string, second half from second string. Remainders discarded.
    a = seedling[0]
    b = seedling[1]
    index = _rand_index(a)
    a_start = a[0:index]
    a_end = a[index:]
    b_start = b[0:index]
    b_end = b[index:]
    a = a_start + b_end
    b = a_end + b_start
    return [a, b]

def _is_crossable(crossover_rate):
    chance_of_crossover = random.uniform(0.0, 1.0)
    if crossover_rate == 0.0:
        return False
    elif chance_of_crossover <= crossover_rate:
        return True

    return False

def _pair_up(pool):
    #pair strings at random for crossover
    return list(map(lambda x: (
        _select_random(pool, _rand_index(pool)),
        _select_random(pool, _rand_index(pool))),
        range(len(pool) / 2)))


def _rand_index(collection):
    #generate random index
    return random.randrange(0, len(collection))


def _select_random(pool, index):
    #select a random index 0 to pool size
    return pool[index]
