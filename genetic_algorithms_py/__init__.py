import mutation
import seeding
import reproduction
import crossover
import debug


def __init__(params):

    debug._remove_fitness_data(params['function_name'])

    seeding_pool = seeding.pool(
        params['pool_size'],
        params['constraint_range'],
        params['number_of_variables'])

    params['pool'] = seeding_pool

    final_pool = _aux(params)
    print reproduction._build_params(final_pool, 0, params['number_of_variables'])

    if debug._is_debugging():
        debug._chart(params['pool_size'], params['function_name'])
    return final_pool


def _aux(aux_params):
    number_of_variables = aux_params['number_of_variables']
    previous_generations_top = []

    for i in range(aux_params['iterations']):
        seed = aux_params['pool']
        test_params = aux_params
        debug._format_output(['{a} Seed'.format(a=i)] + seed,
                             number_of_variables)

        solved, pool = _is_solved(test_params, previous_generations_top)
        previous_generations_top.append(pool)
        if len(previous_generations_top) > 13:
            previous_generations_top.pop(0)
        if solved:
            return pool

        test_params['pool'] = reproduction.reproduce(test_params)
        debug._format_output(['reproduction'] + test_params['pool'],
                             number_of_variables)

        test_params['pool'] = crossover.crossover(test_params)
        debug._format_output(['crossover'] + test_params['pool'],
                             number_of_variables)

        test_params['pool'] = mutation.mutate_pool(
            test_params['pool'], test_params['mutation_probability'])
        debug._format_output(['mutated'] + test_params['pool'],
                             number_of_variables)

        aux_params['pool'] = test_params['pool']
    return previous_generations_top[-1]


def _is_solved(params, previous_generations_top):

    index = 0 if params['max'] else -1
    if all(x == previous_generations_top[0] for x in previous_generations_top) and len(previous_generations_top) >= 10:
        dictionary = reproduction._build_dictionary(params)
        sorted_pool = reproduction._sort_dictionary(dictionary)
        return True, sorted_pool[index]['seed']
    else:
        dictionary = reproduction._build_dictionary(params)
        sorted_pool = reproduction._sort_dictionary(dictionary)

    if params['target'] is not None:
        return _find_target(sorted_pool, params['target'])
    else:
        return False, sorted_pool[index]['seed']


def _find_target(sorted_pool, target):
    if target is 0:
        sorted_pool = list(reversed(sorted_pool))
        return ((sorted_pool[0]['weight']) == 0), sorted_pool[0]['seed']
    else:
        return ((sorted_pool[0]['weight']) >= target), sorted_pool[0]['seed']
