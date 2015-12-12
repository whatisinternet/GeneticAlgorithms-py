import random
import debug
import encoder
from decimal import *


# Select next generation based on objective function's weighted random
# selection output
def reproduce(reproduction_params):

    carry_over = reproduction_params['carry_over']

    sorted_pool = _reject_outliers(
        _sort_dictionary(
            _build_dictionary(reproduction_params)), reproduction_params)

    debug._debug_chart(reproduction_params, sorted_pool, reproduction_params['function_name'])

    total_fitness = _total_fitness(sorted_pool)

    return list(map((lambda x: _select_child(sorted_pool, total_fitness,
                                             reproduction_params)),
                    range(carry_over)))


# private ---
def _build_dictionary(dictionary_params):
    # Select next generation based on objective function's weighted random
    # selection output build a dictionary of probabilities that binary string
    # should be selected. The binary strings correspond 1:1 with their weight

    pool_size = dictionary_params['pool_size']
    number_of_variables = dictionary_params['number_of_variables']
    current_pool = dictionary_params['pool']
    objective_function = dictionary_params['objective_function']

    return list(map((lambda x: {'seed': x,
                                'weight': (objective_function(
                                    *_build_params(x, pool_size,
                                                   number_of_variables)))}),
                    current_pool))


# Big help from: http://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
# for this bit
def _build_params(test, pool_size, number_of_variables):
    a = map("".join, zip(*[iter(test)] * (len(test) / number_of_variables)))
    return map(lambda x: encoder.d(x), a)


# Sort dictionary weights for quicker selection
def _sort_dictionary(dictionary):
    return sorted(dictionary, key=lambda x: x['weight'] / _total_fitness(dictionary), reverse=True)


# Sum total fitness sum and output it
def _total_fitness(dictionary):
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x + y), weights, 0)


def _reject_outliers(dictionary, params):
    safe_range = params['constraint_range']
    safe = [x for x in dictionary if int(encoder.d(x['seed'])) in safe_range]
    if len(safe) == 0:
        return dictionary
    else:
        return safe

# Select string based on objective funstion's probability of being chosen
# TODO: Refactor -- THIS IS BAD
def _select_child(dictionary, total_fitness, params):

    sorted_children = sorted(dictionary, key=lambda x: (x['weight']),
                                reverse=params['max'])

    if params['max']:
        max_weight = sorted_children[0]['weight'] / total_fitness
        min_weight = sorted_children[-1]['weight'] / total_fitness
    else:
        max_weight = sorted_children[-1]['weight'] / total_fitness
        min_weight = sorted_children[0]['weight'] / total_fitness

    if max_weight == min_weight:
        return sorted_children[0]['seed']
    else:
        random_weight = random.uniform(float(min_weight), float(max_weight))
        child = list(filter((lambda x: x['weight'] / total_fitness <= random_weight),
                            sorted_children))
        return child[0]['seed']
