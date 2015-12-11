import random
import encoder


# Create a random binary string 0 to max binary number of given string
# length (ie. 1111)
def initialization_vector(constraint_range, variables):
    return reduce((lambda x, y: x + _seed(constraint_range)),
                  range(variables), "")


# Create a random binary string 0 to max binary number of given string
# length (ie. 1111)
def _seed(constraint_range):
    init_value = random.uniform(long(constraint_range[0]),
                                long(constraint_range[-1]))
    return encoder.e(init_value)
