from genetic_algorithms_py import seeding


def test_it_should_return_an_array_of_string():
    asserted_pool = seeding.pool(8, range(255), 1)
    assert len(asserted_pool) == 8


def test_it_should_only_return_an_array_of_strings_containing_only_1_and_0():
    asserted_pool = seeding.pool(8, range(255), 64)
    for asserted_string in asserted_pool:
        for i in asserted_string:
            assert (i == "1" or i == "0")
