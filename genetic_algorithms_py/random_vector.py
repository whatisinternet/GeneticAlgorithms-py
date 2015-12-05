import random

def initialization_vector(constraint_range, variables):
    #create a random binary string 0 to max binary number of given string length (ie. 1111) 
    return reduce((lambda x, y: x + _seed(constraint_range)),
                  range(variables), "")

def _seed(constraint_range):
    #create a random binary string 0 to max binary number of given string length (ie. 1111)
    max_value = "{0:b}".format(constraint_range[-1])
    init_value = random.uniform(float(constraint_range[0]), float(constraint_range[-1]))
    return "{0:b}".format(abs(int(init_value))).zfill(len(max_value))
