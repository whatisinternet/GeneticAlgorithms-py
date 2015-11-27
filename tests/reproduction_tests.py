from nose.tools import *
import itertools
from genetic_algorithms_py import seeding
from genetic_algorithms_py import reproduction

def test_it_should_return_an_array_of_size_8():
    seeding_pool = seeding.pool(8)
    asserted_pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    assert len(asserted_pool) == 8

def test_it_should_return_an_array_of_strings():
    seeding_pool = seeding.pool(8)
    asserted_pool = reproduction.reproduce((lambda x: int(x, 2) ** 2), seeding_pool)
    for asserted in asserted_pool:
        assert isinstance( asserted, str )

# Testing private methods NB: Wouldn't normally keep these

def test__build_dictionary_should_return_a_collection_of_size_8():
    seeding_pool = seeding.pool(8)
    asserted_dictionary = reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    assert len(asserted_dictionary) == 8

def test__build_dictionary_should_return_a_collection_of_dictionaries():
    seeding_pool = seeding.pool(8)
    asserted_dictionary= reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    for asserted in asserted_dictionary:
        assert isinstance(asserted, dict)

def test__build_dictionary_should_return_a_collection_of_dictionaries_with_key_seed():
    seeding_pool = seeding.pool(8)
    asserted_dictionary= reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    for asserted in asserted_dictionary:
        assert isinstance(asserted['seed'], str)

def test__build_dictionary_should_return_a_collection_of_dictionaries_with_key_weight():
    seeding_pool = seeding.pool(8)
    asserted_dictionary= reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    for asserted in asserted_dictionary:
        assert isinstance(asserted['weight'], int)

def test__sort_dictionary_should_sort_the_collection_by_weight_decending():
    seeding_pool = seeding.pool(8)
    dictionary= reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    asserted_dictionary = reproduction._sort_dictionary(dictionary)
    asserted_values = reversed(list(map((lambda x: x['weight']), asserted_dictionary)))
    it = iter(asserted_values)
    it.next()
    is_sorted = all(b >= a for a, b in itertools.izip(asserted_values, it))
    assert is_sorted == True

def test__total_fitness():
    seeding_pool = seeding.pool(8)
    dictionary = reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    asserted_total = reproduction._total_fitness(dictionary)
    assert isinstance(asserted_total, int)

def test__select_child():
    seeding_pool = seeding.pool(8)
    dictionary = reproduction._build_dictionary((lambda x: int(x, 2) ** 2), seeding_pool)
    total_fitness = reproduction._total_fitness(dictionary)
    asseted_child = reproduction._select_child(dictionary, total_fitness)
    assert isinstance(asseted_child, str)
