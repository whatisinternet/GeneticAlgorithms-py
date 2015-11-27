import random

def initialization_vector():
    init_value= random.randrange(0,255)
    return "{0:b}".format(init_value).zfill(8)
