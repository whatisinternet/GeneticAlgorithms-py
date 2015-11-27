def reproduce( objective_function, current_pool, target):
    return _build_dictionary( objective_function, current_pool )


def _build_dictionary( objective_function, current_pool ):
    return list(map((lambda x: {'seed': x, 'weight': objective_function(x)}),
        current_pool))
