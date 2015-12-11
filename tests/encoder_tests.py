from genetic_algorithms_py import encoder
from decimal import *


def test_encode_to_binary():
    asserted_string = encoder.e(-13.234523452345)
    print asserted_string
    for i in asserted_string:
        assert (i == "1" or i == "0")


def test_decode_to_float():
    asserted_float = encoder.d('1111111111111111111111111111111111111111111111100101100001001010')
    assert isinstance(asserted_float, Decimal) == True

