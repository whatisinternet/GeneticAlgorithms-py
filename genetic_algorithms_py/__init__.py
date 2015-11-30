import mutation
import seeding
import reproduction
import crossover
import plotter
import os

def __init__(black_box, iterations, bit_size,
        target = None, function_name = None):
    _remove_fitness_data()

    if target == None:
        target = reduce( lambda x, y: x + y ** 2, range(bit_size))

    seeding_pool = seeding.pool(8, bit_size)
    final_pool, state = _aux(seeding_pool, black_box, 0, iterations, target)
    if _is_debugging():
        print seeding_pool
        print final_pool, state
        _debug_chart(target, function_name)
    return final_pool


def _aux(seed, black_box, depth, max_iterations, target):
    _format_output(['{a} Seed'.format(a=depth)] + seed)
    if depth == max_iterations:
        return seed, "NOT FOUND!"
    elif target in seed:
        return seed, "FOUND!"
    else:
        pool = reproduction.reproduce(black_box, seed)
        _format_output(['reproduction'] + pool)
        crossed_over = crossover.crossover(pool)
        _format_output(['crossover'] + crossed_over)
        mutated = mutation.mutate_pool(crossed_over)
        _format_output(['mutated'] + mutated)
        return _aux(mutated, black_box, depth + 1, max_iterations, target)

def _debug_chart(target, function_name):
    plotter.chart(target, function_name)

def _is_debugging():
    f = open('./debug','r')
    debug = f.readline()
    if debug  == "True\n":
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
