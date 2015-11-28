from genetic_algorithms_py import random_vector

def pool(size, bit_size):
    return list(
            map(
                (lambda x:
                    random_vector.initialization_vector(bit_size)),
                range(size)
                )
            )
