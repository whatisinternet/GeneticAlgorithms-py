import random


# Mutate a string with an input probability of being mutated or not
def mutate_pool(pool, mutation_probability):
    return list(map(lambda x: mutate(x, mutation_probability), pool))


# Select a random bit of one of the binary strings and flip the bit
def mutate(seed, mutation_probability=0.0):

    if _is_mutable(mutation_probability):
        iterations = int(random.randrange(0, len(seed)))
        return _mutate_aux(seed, iterations)

    else:
        return seed


def _mutate_aux(seed, iterations):

    listified_seed = list(seed)

    for i in range(iterations):

        index = random.randrange(0, len(seed))
        listified_seed[index] = str(1 - int(seed[index]))

    return "".join(listified_seed)


def _is_mutable(mutation_probability):
    chance_of_mutation = random.uniform(0.0, 1.0)
    if mutation_probability == 0.0:
        return False
    elif chance_of_mutation <= mutation_probability:
        return True

    return False
