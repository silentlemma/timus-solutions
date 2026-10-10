import sys
from collections import Counter

HEADER = 3  # N, M and P come before the grid


def main():
    data = sys.stdin.read().split()
    n, p = int(data[0]), int(data[2])
    # the words take their letters out of the grid one cell each, so what is
    # left does not depend on where they lie
    left = Counter("".join(data[HEADER : HEADER + n]))
    left.subtract("".join(data[HEADER + n : HEADER + n + p]))
    print("".join(c * left[c] for c in sorted(left)))


main()
