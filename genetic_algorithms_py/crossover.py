import random


def crossover(pool, rate):
    crossed = map(lambda x: _cross(x, rate), _pair_up(pool))
    return sum(crossed, [])


# Private ----
def _cross(seedling, rate):
    test_rate = random.uniform(0.0, 1.0)
    a = seedling[0]
    b = seedling[1]
    if test_rate <= rate:
        index = _rand_index(a)
        a_start = a[0:index]
        a_end = a[index:]
        b_start = b[0:index]
        b_end = b[index:]
        a = a_start + b_end
        b = a_end + b_start
    return [a, b]


def _pair_up(pool):
    return list(map(lambda x: (
        _select_random(pool, _rand_index(pool)),
        _select_random(pool, _rand_index(pool))),
        range(len(pool) / 2)))


def _rand_index(collection):
    return random.randrange(0, len(collection))


def _select_random(pool, index):
    return pool[index]
