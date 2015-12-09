import random
import debug


# Select next generation based on objective function's weighted random
# selection output
def reproduce(reproduction_params):

    carry_over = reproduction_params['carry_over']

    sorted_pool = _sort_dictionary(_build_dictionary(reproduction_params))

    debug._debug_chart(reproduction_params, sorted_pool)

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


def _build_params(test, pool_size, number_of_variables):
    return map("".join, zip(*[iter(test)] * (len(test) / number_of_variables)))


# Sort dictionary weights for quicker selection
def _sort_dictionary(dictionary):
    return sorted(dictionary, key=lambda x: x['weight'], reverse=True)


# Sum total fitness sum and output it
def _total_fitness(dictionary):
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x+abs(y)), weights, 0)


# Select string based on objective funstion's probability of being chosen
# TODO: Refactor -- THIS IS BAD
def _select_child(dictionary, total_fitness, params):
    if params['max'] == True:
        selector = 0
    else:
        selector = -1

    if total_fitness is 0:
        return dictionary[selector]['seed']
    else:
        sorted_children = sorted(dictionary, key=lambda x: (x['weight']),
                                 reverse=True)

        max_weight = sorted_children[0]['weight']
        min_weight = sorted_children[-1]['weight']
        if max_weight == min_weight:
            return sorted_children[selector]['seed']
        else:
            random_weight = random.randrange(min_weight, max_weight)
            child = list(filter((lambda x: x['weight'] <= random_weight),
                                sorted_children))
            return child[selector]['seed']
