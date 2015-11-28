from nose.tools import *
import genetic_algorithms_py

black_box = (lambda x: int(x, 2) ** 2)
black_box = (lambda vector: reduce(lambda x, y: int(y) + int(x) ** 2, vector))

def test_it_should_get_an_initialization_vector():
    assert isinstance(
            genetic_algorithms_py.__init__(black_box, 1, 64, None),
            list)
