from genetic_algorithms_py import random_vector


# Generate a random initial seed pool of random binary strings
def pool(size, constraint_range, number_of_variables):
    return list(map((lambda x:
                    random_vector.initialization_vector(constraint_range,
                                                        number_of_variables)),
                range(size)))
