from os import _exit, write

WORD_BITS = 64
RADIX = 1 << WORD_BITS
DIGIT_MASK = RADIX - 1

DENOMINATOR = RADIX * RADIX - RADIX - 1


def count(stripes):
    encoded = (1 << (WORD_BITS * (stripes + 1))) // DENOMINATOR
    return 2 * (encoded & DIGIT_MASK)


def main():
    stripes = int(open(0, "rb", buffering=0).read())
    write(1, (str(count(stripes)) + "\n").encode())
    _exit(0)


main()
