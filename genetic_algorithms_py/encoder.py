from bitstring import BitArray

multiplier = 9681968.0

def e(value):
    converted = int(value * multiplier)
    return BitArray(int=converted, length=48).bin

def d(value):
    decoded_integer = BitArray(bin=value).int
    return float(decoded_integer / multiplier)
