import mutation
import seeding
import reproduction
import crossover
import debug
import os


def __init__(params):

    debug._remove_fitness_data()

    seeding_pool = seeding.pool(
        params['pool_size'],
        params['constraint_range'],
        params['number_of_variables'])

    params['pool'] = seeding_pool

    final_pool = _aux(params)

    if debug._is_debugging():
        print _final(seeding_pool)
        print _final(final_pool)
        debug._chart(pool_size, params['function_name'])
    return final_pool


def _aux(aux_params):
    number_of_variables = aux_params['number_of_variables']

    for i in range(aux_params['iterations']):
        seed = aux_params['pool']
        test_params = aux_params
        debug._format_output(['{a} Seed'.format(a=i)] + seed, number_of_variables)

        test_params['pool'] = reproduction.reproduce(test_params)
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return reproduction_pool
        debug._format_output(['reproduction'] + test_params['pool'], number_of_variables)

        test_params['pool'] = crossover.crossover(test_params)
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return crossed_over
        debug._format_output(['crossover'] + test_params['pool'], number_of_variables)

        test_params['pool'] = mutation.mutate_pool(test_params['pool'], test_params['mutation_probability'])
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return mutated
        debug._format_output(['mutated'] + test_params['pool'], number_of_variables)

        aux_params['pool'] = test_params['pool']
    return aux_params['pool']


def _is_solved(params):

    dictionary = reproduction._build_dictionary(params)
    sorted_pool = reproduction._sort_dictionary(dictionary)
    if debug._is_debugging():
        print sorted_pool
    if params['target'] is not None:
        return _find_target(sorted_pool, params['target'])
    else:
        return False, sorted_pool[0]['seed']

def _find_target(sorted_pool, target):
    if target is 0:
        sorted_pool = list(reversed(sorted_pool))
        return ((sorted_pool[0]['weight'] ) == 0), sorted_pool[0]['seed']
    else:
        return ((sorted_pool[0]['weight']) >= target), sorted_pool[0]['seed']


def _final(collection):
    return list(map((lambda x: int(x,2)), collection))
