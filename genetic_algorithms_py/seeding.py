from genetic_algorithms_py import random_vector

def pool(size):
    return list(
            map(
                (lambda x:
                    random_vector.initialization_vector()),
                range(size)
                )
            )
