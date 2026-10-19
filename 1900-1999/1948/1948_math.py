import math
import sys

SQUARE_FACTOR = 3
CONSTANT_FACTOR = 12
INPUT_FIELDS = 3


def solve(a, b, c):
    scaled = SQUARE_FACTOR * b * b // a - CONSTANT_FACTOR * c
    if scaled < 0:
        return 1
    threshold = scaled // a + 1
    return math.isqrt(threshold) + 1


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    cases = data[0]
    output = []
    for index in range(cases):
        start = 1 + INPUT_FIELDS * index
        output.append(str(solve(*data[start : start + INPUT_FIELDS])))
    print("\n".join(output))


if __name__ == "__main__":
    main()
