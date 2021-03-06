import os
import plotter
import reproduction
import encoder


def _format_output(collection, number_of_variables):
    if not _is_debugging():
        joined = ",".join(collection[1:])
        print "{a},{b}".format(a=collection[0], b=joined)


def _chart(pool_size, function_name):
    plotter.chart(pool_size, function_name)


def _is_debugging():
    f = open('./debug', 'r')
    debug = f.readline()
    if debug == "True\n":
        return True
    else:
        return False


def _remove_fitness_data(function_name):
    if _is_debugging():
        try:
            os.remove('./data/fitness_data{a}.csv'.format(a=function_name))
        except OSError:
            pass


def _debug_chart(reproduction_params, sorted_pool, function_name):
    number_of_variables = reproduction_params['number_of_variables']
    maximize = reproduction_params['max']

    if _is_debugging():
        _save_fitnesses(sorted_pool, number_of_variables, function_name, maximize)


def _save_fitnesses(data, number_of_variables, function_name, maximize=True):
    if _is_debugging():
        if maximize == True:
            best = data[0]
        else:
            best = data[-1]
        f = open('./data/fitness_data{a}.csv'.format(a=function_name), 'a+')
        decoded_seed = reproduction._build_params(best['seed'], 0,
                                                  number_of_variables)
        for a in decoded_seed:
            print a, best['weight']
            f.write("{a},{b}\n".format(a=a, b=best['weight']))

