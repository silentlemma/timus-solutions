from os import _exit, write
from sys import stdin

DATA = 4
CHECKS = 3
BITS = DATA + CHECKS
ZERO = ord("0")
DATA_MASK = (1 << DATA) - 1
ALL_CHECKS = (1 << CHECKS) - 1
CHECK_MASKS = tuple((DATA_MASK ^ (1 << check)) | (1 << (DATA + check)) for check in range(CHECKS))


def restore(data):
    word = 0
    for position, token in enumerate(data.split()):
        word |= (token[-1] - ZERO) << position
    syndrome = 0
    for check, mask in enumerate(CHECK_MASKS):
        syndrome |= ((word & mask).bit_count() & 1) << check
    if syndrome:
        if syndrome & (syndrome - 1) == 0:
            position = DATA + syndrome.bit_length() - 1
        elif syndrome == ALL_CHECKS:
            position = DATA - 1
        else:
            position = (ALL_CHECKS ^ syndrome).bit_length() - 1
        word ^= 1 << position
    output = bytearray(b"0 0 0 0 0 0 0\n")
    for position in range(BITS):
        output[2 * position] += (word >> position) & 1
    return output


def main():
    write(1, restore(stdin.buffer.read()))
    _exit(0)


main()
