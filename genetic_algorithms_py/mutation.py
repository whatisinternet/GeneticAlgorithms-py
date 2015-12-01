import random


def mutate_pool(pool, mutation_probability):
    return list(map(lambda x: mutate(x, mutation_probability), pool))


def mutate(seed, mutation_probability):
    chance_of_mutation = random.randrange(0, len(seed)) / len(seed)

    if chance_of_mutation > mutation_probability:

        iterations = random.randrange(0, len(seed))
        listified_seed = list(seed)
        for i in range(iterations):
            index = random.randrange(0, len(seed))
            listified_seed[index] = str(1 - int(seed[index]))
        return "".join(listified_seed)
    else:
        return seed
