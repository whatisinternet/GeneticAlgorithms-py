import random

def initialization_vector(bit_size):
    max_val = reduce( lambda x, y: x + y ** 2, range(bit_size))
    init_value= random.randrange(0,max_val)
    return "{0:b}".format(init_value).zfill(bit_size)
