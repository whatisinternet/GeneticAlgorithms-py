import random
import plotter


def reproduce(objective_function, current_pool, pool_size):
    sorted_pool = _sort_dictionary(_build_dictionary(objective_function,
                                                     current_pool, pool_size))
    _debug_chart(pool_size, sorted_pool)
    total_fitness = _total_fitness(sorted_pool)
    return list(map((lambda x: _select_child(sorted_pool, total_fitness)),
                    range(len(sorted_pool))))


# private ---
def _debug_chart(pool_size, sorted_pool):
    f = open('./debug', 'r')
    debug = f.readline()
    if debug == "True\n":
        plotter.save_fitnesses(sorted_pool)


def _build_dictionary(objective_function, current_pool, pool_size):
    return list(map((lambda x: {'seed': x,
                                'weight': objective_function(*_build_params(x, pool_size))}),
                    current_pool))

def _build_params(test, pool_size):
    return list(map(lambda x: test, range(pool_size)))

def _sort_dictionary(dictionary):
    return sorted(dictionary, key=lambda x: x['weight'], reverse=True)


def _total_fitness(dictionary):
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x+y), weights, 0)


def _select_child(dictionary, total_fitness):
    selected_precentage = random.uniform(0, 100)
    sorted_children = sorted(dictionary,
                             key=lambda x: (x['weight'] / total_fitness) %
                             selected_precentage, reverse=True)
    return sorted_children[0]['seed']
