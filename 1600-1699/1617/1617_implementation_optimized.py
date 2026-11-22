from os import _exit, write

WEIGHT_VALUES = 101
GROUP_SIZE = 4
MIN_DIAMETER = 600


def main():
    values = map(int, open(0, "rb", buffering=0).read().split())
    next(values)  # The remaining tokens are the declared n wheel-pair diameters.
    frequencies = [0] * WEIGHT_VALUES
    for diameter in values:
        frequencies[diameter - MIN_DIAMETER] += 1
    answer = sum(frequency // GROUP_SIZE for frequency in frequencies)
    write(1, (str(answer) + "\n").encode())
    _exit(0)


main()
