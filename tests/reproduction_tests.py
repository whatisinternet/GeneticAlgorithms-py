import itertools
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction

black_box = (lambda x, y: y + x ** 2)

params = {'objective_function': black_box,
          'pool': seeding.pool(8, range(255), 2),
          'pool_size': 64,
          "constraint_range": range(-6, 6),
          'number_of_variables': 2,
          'max': True,
          'function_name': 'NoseTests',
          'carry_over': 2}


def test_it_should_return_an_array_of_strings():
    asserted_pool = reproduction.reproduce(params)
    for asserted in asserted_pool:
        assert isinstance(asserted, str)


def test_it_should_return_an_array_of_strings_of_length_8():
    params['carry_over'] = 32
    for i in range(10):
        asserted_pool = reproduction.reproduce(params)
        assert len(asserted_pool) == 32


# Testing private methods NB: Wouldn't normally keep these
def test__build_dictionary_should_return_a_collection_of_size_8():
    asserted_dictionary = reproduction._build_dictionary(params)
    assert len(asserted_dictionary) >= 2


def test__build_dictionary_should_return_a_collection_of_dictionaries():
    asserted_dictionary = reproduction._build_dictionary(params)
    for asserted in asserted_dictionary:
        assert isinstance(asserted, dict)


def test__build_dictionary_should_return_a_collection_of_dictionaries_with_key_seed():
    asserted_dictionary = reproduction._build_dictionary(params)
    for asserted in asserted_dictionary:
        assert isinstance(asserted['seed'], str)


def test__build_dictionary_should_return_a_collection_of_dictionaries_with_key_weight():
    asserted_dictionary = reproduction._build_dictionary(params)
    for asserted in asserted_dictionary:
        assert not isinstance(asserted['weight'], str)


def test__sort_dictionary_should_sort_the_collection_by_weight_decending():
    dictionary= reproduction._build_dictionary(params)
    asserted_dictionary = reproduction._sort_dictionary(dictionary)
    asserted_values = reversed(list(map((lambda x: x['weight']),
                                        asserted_dictionary)))
    it = iter(asserted_values)
    it.next()
    is_sorted = all(b >= a for a, b in itertools.izip(asserted_values, it))
    assert is_sorted is True


def test__total_fitness():
    dictionary= reproduction._build_dictionary(params)
    asserted_total = reproduction._total_fitness(dictionary)
    assert not isinstance(asserted_total, str)


def test__select_child():
    dictionary= reproduction._build_dictionary(params)
    total_fitness = reproduction._total_fitness(dictionary)
    asseted_child = reproduction._select_child(dictionary, total_fitness, params)
    assert isinstance(asseted_child, str)
