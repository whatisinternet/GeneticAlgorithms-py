import random


# Create a random binary string 0 to max binary number of given string
# length (ie. 1111)
def initialization_vector(constraint_range, variables):
    return reduce((lambda x, y: x + _seed(constraint_range)),
                  range(variables), "")


# Create a random binary string 0 to max binary number of given string
# length (ie. 1111)
def _seed(constraint_range):
    max_value = "{0:b}".format(constraint_range[-1])
    init_value = random.uniform(float(constraint_range[0]),
                                float(constraint_range[-1]))
    return "{0:b}".format(abs(int(init_value))).zfill(len(max_value))
