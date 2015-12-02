import genetic_algorithms_py

black_box = (lambda x, y: int(y, 2) + int(x, 2) ** 2)


def test_it_should_get_an_initialization_vector():
    assert isinstance(genetic_algorithms_py.__init__(black_box, 1, range(8),
                                                     2, 0.0, 2, 8, None),
                      list)

def test_it_should_fail():
    assert isinstance(genetic_algorithms_py.__init__(black_box, 1, range(8),
                                                     2, 0.0, 2, 0, None),
                      bool)
