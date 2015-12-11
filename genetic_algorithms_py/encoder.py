from bitstring import BitArray
from decimal import *

multiplier = 96868.0

def e(value):
    converted = long(Decimal(value) * Decimal(multiplier))
    return BitArray(int=converted, length=48).bin

def d(value):
    decoded_integer = BitArray(bin=value).int
    return Decimal(Decimal(decoded_integer) / Decimal(multiplier))
