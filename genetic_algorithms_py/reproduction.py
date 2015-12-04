import plotter


def reproduce(reproduction_params):
    carry_over = reproduction_params['carry_over']

    sorted_pool = _sort_dictionary(_build_dictionary(reproduction_params))

    _debug_chart(reproduction_params, sorted_pool)

    total_fitness = _total_fitness(sorted_pool)

    return list(map((lambda x: _select_child(sorted_pool, total_fitness)),
                    range(carry_over)))


# private ---
def _build_dictionary(dictionary_params):
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


def _sort_dictionary(dictionary):
    return sorted(dictionary, key=lambda x: x['weight'], reverse=True)


def _total_fitness(dictionary):
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x+abs(y)), weights, 0)


def _select_child(dictionary, total_fitness):
    if total_fitness is 0:
        return dictionary[0]['seed']
    else:
        sorted_children = sorted(dictionary,
                                key=lambda x: (x['weight'] / total_fitness)
                                , reverse=True)
        return sorted_children[0]['seed']


def _debug_chart(reproduction_params, sorted_pool):
    pool_size = reproduction_params['pool_size']
    number_of_variables = reproduction_params['number_of_variables']

    f = open('./debug', 'r')
    debug = f.readline()
    if debug == "True\n":
        plotter.save_fitnesses(sorted_pool, number_of_variables)


