from genetic_algorithms_py import random_vector


def test_it_should_return_a_string():
    assert isinstance(random_vector.initialization_vector(range(8), 2),
                      basestring)


def test_it_should_only_return_a_string_of_1_and_0():
    asserted_string = random_vector.initialization_vector(range(8), 2)
    for i in asserted_string:
        assert (i == "1" or i == "0")


def test_it_should_return_a_string_of_16_characters():
    for i in range(1000):
        asserted_string = random_vector.initialization_vector(range(255), 2)
        assert len(asserted_string) == 16
