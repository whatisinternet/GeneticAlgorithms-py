import genetic_algorithms_py

black_box = (lambda x, y: int(y) + int(x) ** 2)


def test_it_should_get_an_initialization_vector():
    assert isinstance(genetic_algorithms_py.__init__(black_box, 1, 8, 2, None),
                      list)
