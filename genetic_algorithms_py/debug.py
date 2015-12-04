import reproduction

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


def _remove_fitness_data():
    if _is_debugging():
        try:
            os.remove('./fitness_data.csv')
        except OSError:
            pass


def _debug_chart(reproduction_params, sorted_pool):
    pool_size = reproduction_params['pool_size']
    number_of_variables = reproduction_params['number_of_variables']

    if _is_debugging():
        _save_fitnesses(sorted_pool, number_of_variables)


def _save_fitnesses(data, number_of_variables):
    if _is_debugging():
        x = list(map(lambda x:
                    reproduction._build_params(x['seed'], 0, number_of_variables),
                    data))
        y = list(map(lambda x: x['weight'], data))
        f = open('./fitness_data.csv', 'a+')

        for i in range(len(x)):
            for idx in range(len(x[i])):
                f.write("{a},{b}\n".format(a=int(x[i][idx], 2), b=y[i]))
