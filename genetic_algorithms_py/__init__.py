import mutation
import seeding
import reproduction
import crossover
import plotter
import os


def __init__(black_box, iterations, bit_size,
             pool_size, mutation_probability, function_name=None):
    _remove_fitness_data()

    seeding_pool = seeding.pool(pool_size, bit_size)
    final_pool = _aux(seeding_pool, black_box, 0, iterations, pool_size, mutation_probability)
    if _is_debugging():
        print seeding_pool
        print final_pool
        _debug_chart(pool_size, function_name)
    return final_pool


def _aux(seed, black_box, depth, max_iterations, pool_size, mutation_probability):
    _format_output(['{a} Seed'.format(a=depth)] + seed)
    if depth == max_iterations:
        return seed
    else:
        pool = reproduction.reproduce(black_box, seed, pool_size)
        _format_output(['reproduction'] + pool)
        crossed_over = crossover.crossover(pool)
        _format_output(['crossover'] + crossed_over)
        mutated = mutation.mutate_pool(crossed_over, mutation_probability)
        _format_output(['mutated'] + mutated)
        return _aux(mutated, black_box, depth + 1, max_iterations, pool_size, mutation_probability)


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


def _format_output(collection):
    print ",".join(collection)
