import random

def initialization_vector(constraint_range, variables):
    return reduce((lambda x, y: x + _seed(constraint_range)),
                  range(variables), "")

def _seed(constraint_range):
    max_value = "{0:b}".format(constraint_range[-1])
    init_value = random.randrange(constraint_range[0], constraint_range[-1])
    return "{0:b}".format(init_value).zfill(len(max_value))
