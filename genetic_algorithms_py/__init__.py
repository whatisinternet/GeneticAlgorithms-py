import mutation
import seeding
import reproduction
import crossover
import plotter
import os


def __init__(black_box, iterations, constraint_range,
             pool_size, mutation_probability, number_of_variables, target,
             function_name=None):

    _remove_fitness_data()

    seeding_pool = seeding.pool(pool_size, constraint_range, number_of_variables)

    final_pool = _aux(seeding_pool, black_box, 0, iterations,
                      mutation_probability, number_of_variables, pool_size, target)
    if _is_debugging():
        print _final(seeding_pool)
        print _final(final_pool)
        _debug_chart(pool_size, function_name)
    return final_pool


def _aux(seed, black_box, depth, max_iterations,
         mutation_probability, number_of_variables, pool_size, target):

    solved, pool = _is_solved(black_box, seed, pool_size, number_of_variables, target)
    if solved:
        print solved, pool
        return pool

    for i in range(max_iterations):
        _format_output(['{a} Seed'.format(a=i)] + seed, number_of_variables)

        pool = reproduction.reproduce(black_box, seed,
                                      pool_size, number_of_variables)

        solved, seed = _is_solved(black_box, pool, pool_size, number_of_variables, target)
        if solved:
            print solved, seed
            return pool
        _format_output(['reproduction'] + pool, number_of_variables)

        crossed_over = crossover.crossover(pool)
        solved, seed = _is_solved(black_box, crossed_over, pool_size, number_of_variables, target)
        if solved:
            print solved, seed
            return pool
        _format_output(['crossover'] + crossed_over, number_of_variables)

        mutated = mutation.mutate_pool(crossed_over, mutation_probability)
        solved, seed = _is_solved(black_box, mutated, pool_size, number_of_variables, target)
        if solved:
            print solved, seed
            return pool
        _format_output(['mutated'] + mutated, number_of_variables)

        seed = mutated
    return seed

def _is_solved(black_box, current_pool, pool_size, number_of_variables, target):
    dictionary = reproduction._build_dictionary(black_box, current_pool, pool_size, number_of_variables)
    sorted_pool = reproduction._sort_dictionary(dictionary)
    if _is_debugging():
        print sorted_pool
    if target is not None:
        if target is 0:
            sorted_pool = list(reversed(sorted_pool))
            return ((sorted_pool[0]['weight'] ) == 0), sorted_pool[0]['seed']
        else:
            return ((sorted_pool[0]['weight']) >= target), sorted_pool[0]['seed']
    else:
        return False, sorted_pool[0]['seed']

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
