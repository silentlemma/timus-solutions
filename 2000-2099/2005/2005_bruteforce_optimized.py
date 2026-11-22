from itertools import permutations
from os import _exit, write

POINTS = 5
FIRST = 1
FORBIDDEN_LAST = 2
LAST = POINTS - 2


def main():
    costs = list(map(int, open(0, "rb", buffering=0).read().split()))
    best = route = None
    for a, b, c in permutations(range(FIRST, LAST + 1)):
        if c == FORBIDDEN_LAST:
            continue
        cost = (
            costs[a]
            + costs[POINTS * a + b]
            + costs[POINTS * b + c]
            + costs[POINTS * c + POINTS - 1]
        )
        if best is None or cost < best:
            best, route = cost, (a + 1, b + 1, c + 1)
    answer = str(best) + "\n1 " + " ".join(map(str, route)) + " 5\n"
    write(1, answer.encode())
    _exit(0)


main()
