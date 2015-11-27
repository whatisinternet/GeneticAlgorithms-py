import random

def mutate_pool(pool):
    return list(map(lambda x: mutate(x), pool))

def mutate(seed):
    iterations = random.randrange(0, len(seed))
    listified_seed = list(seed)
    for i in range(iterations):
        index = random.randrange(0, len(seed))
        listified_seed[index] = str(1 - int(seed[index]))
    return "".join(listified_seed)
