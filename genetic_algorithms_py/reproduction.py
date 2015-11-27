import seeding

def reproduce( objective_function, current_pool, target):
    sorted_pool = _sort_dictionary(_build_dictionary( objective_function, current_pool ))
    total_fitness = _total_fitness(sorted_pool)
    return current_pool


# private ---
def _build_dictionary( objective_function, current_pool ):
    return list(map((lambda x: {'seed': x, 'weight': objective_function(x)}),
        current_pool))

def _sort_dictionary( dictionary ):
    return sorted(dictionary, key=lambda x: x['weight'], reverse=True)

def _total_fitness( dictionary ):
    weights = list(map((lambda x: x['weight']), dictionary))
    return reduce((lambda x, y: x+y), weights)
