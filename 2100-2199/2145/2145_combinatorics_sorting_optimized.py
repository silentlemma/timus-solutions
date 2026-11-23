import os
from itertools import islice
import sys


def main():
    values = map(int, sys.stdin.buffer.read().split())
    n = next(values)
    a = sorted(islice(values, n))
    b = sorted(islice(values, n))
    p = next(values)
    # The i-th weakest student can take any of the problems they can solve,
    # except the i problems already taken by weaker students.
    ways = 1 % p
    solvable = 0
    for i, knowledge in enumerate(a):
        while solvable < n and b[solvable] <= knowledge:
            solvable += 1
        ways = ways * (solvable - i) % p
        if ways == 0:
            break
    print(ways)


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
