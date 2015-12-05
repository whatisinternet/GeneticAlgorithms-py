import debug

def reproduce(reproduction_params):
    #select next generation based on objective function's weighted random selection output 
    
    carry_over = reproduction_params['carry_over']

    sorted_pool = _sort_dictionary(_build_dictionary(reproduction_params))

    debug._debug_chart(reproduction_params, sorted_pool)

    total_fitness = _total_fitness(sorted_pool)

    return list(map((lambda x: _select_child(sorted_pool, total_fitness)),
                    range(carry_over)))


# private ---
def _build_dictionary(dictionary_params):
    #select next generation based on objective function's weighted random selection output
    #build a dictionary of probabilities that binary string should be selected.
    #The binary strings correspond 1:1 with their weight
    
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
    #sort dictionary weights for quicker selection
    return sorted(dictionary, key=lambda x: x['weight'], reverse=True)


def _total_fitness(dictionary):
    #sum total fitness sum and output it
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x+abs(y)), weights, 0)


def _select_child(dictionary, total_fitness):
    #select string based on objective funstion's probability of being chosen
    if total_fitness is 0:
        return dictionary[0]['seed']
    else:
        sorted_children = sorted(dictionary,
                                key=lambda x: (x['weight'] / total_fitness)
                                , reverse=True)
        return sorted_children[0]['seed']


