from genetic_algorithms_py import random_vector


def pool(size, constraint_range, number_of_variables):
    #generate a random initial seed pool of random binary strings
    return list(map((lambda x:
                    random_vector.initialization_vector(constraint_range,
                                                        number_of_variables)),
                range(size)))
