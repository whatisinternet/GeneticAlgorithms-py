from bitstring import BitArray

multiplier = 96868.0

def e(value):
    converted = long(value * multiplier)
    return BitArray(int=converted, length=48).bin

def d(value):
    decoded_integer = BitArray(bin=value).int
    return float(float(format(float(decoded_integer), '.16g')) / multiplier)
