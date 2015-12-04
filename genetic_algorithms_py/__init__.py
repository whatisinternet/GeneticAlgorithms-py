import mutation
import seeding
import reproduction
import crossover
import plotter
import os


def __init__(params):

    _remove_fitness_data()

    seeding_pool = seeding.pool(
        params['pool_size'],
        params['constraint_range'],
        params['number_of_variables'])

    params['pool'] = seeding_pool

    final_pool = _aux(params)

    if _is_debugging():
        print _final(seeding_pool)
        print _final(final_pool)
        _debug_chart(pool_size, params['function_name'])
    return final_pool


def _aux(aux_params):
    number_of_variables = aux_params['number_of_variables']

    solved, pool = _is_solved(aux_params)
    if solved:
        print solved, pool
        return aux_params['seed']

    for i in range(aux_params['iterations']):
        seed = aux_params['pool']
        test_params = aux_params
        _format_output(['{a} Seed'.format(a=i)] + seed, number_of_variables)

        test_params['pool']= reproduction.reproduce(aux_params)
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return reproduction_pool
        _format_output(['reproduction'] + test_params['pool'], number_of_variables)

        test_params['pool'] = crossover.crossover(aux_params['pool'], aux_params['crossover_rate'])
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return crossed_over
        _format_output(['crossover'] + test_params['pool'], number_of_variables)

        test_params['pool'] = mutation.mutate_pool(aux_params['pool'], aux_params['mutation_probability'])
        solved, pool = _is_solved(test_params)
        if solved:
            print solved, pool
            return mutated
        _format_output(['mutated'] + test_params['pool'], number_of_variables)

        aux_params['pool'] = test_params['pool']
    return aux_params['pool']


def _is_solved(params):

    dictionary = reproduction._build_dictionary(params)
    sorted_pool = reproduction._sort_dictionary(dictionary)
    if _is_debugging():
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


def _debug_chart(pool_size, function_name):
    plotter.chart(pool_size, function_name)


def _is_debugging():
    f = open('./debug', 'r')
    debug = f.readline()
    if debug == "True\n":
        return True
    else:
        return False


def _remove_fitness_data():
    if _is_debugging():
        try:
            os.remove('./fitness_data.csv')
        except OSError:
            pass


def _format_output(collection, number_of_variables):
    joined = ",".join(collection[1:])
    print "{a},{b}".format(a=collection[0], b=joined)


def _final(collection):
    return list(map((lambda x: int(x,2)), collection))
