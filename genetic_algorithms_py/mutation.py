import random


def mutate_pool(pool, mutation_probability):
    return list(map(lambda x: mutate(x, mutation_probability), pool))


def mutate(seed, mutation_probability=0.0):
    chance_of_mutation = random.uniform(0.0, mutation_probability)
    iterations = int(random.randrange(0, len(seed)) * chance_of_mutation)
    listified_seed = list(seed)
    for i in range(iterations):
        index = random.randrange(0, len(seed))
        listified_seed[index] = str(1 - int(seed[index]))
    return "".join(listified_seed)
