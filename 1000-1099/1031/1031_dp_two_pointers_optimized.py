import os
from array import array
import sys

INPUT_BUFFER_BYTES = 4096
ASCII_SPACE = ord(" ")

KINDS = 3
# the input: lengths, prices, then N and the two stations, then positions
PRICES = KINDS
QUERY = 2 * KINDS
POSITIONS = QUERY + 3


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > ASCII_SPACE else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, words())
    length = [next(values) for _ in range(KINDS)]
    price = [next(values) for _ in range(KINDS)]
    n, a, b = next(values), next(values), next(values)
    x = array("Q", [0, 0])
    x.extend(next(values) for _ in range(n - 1))
    a, b = min(a, b), max(a, b)
    # cost[i]: the cheapest way from a to i; it never decreases along the
    # line, so for every kind of ticket the farthest start in reach is best
    cost = array("Q", [0]) * (n + 1)
    start = [a] * KINDS
    kinds = list(zip(range(KINDS), length, price))
    for i in range(a + 1, b + 1):
        best = None
        for k, reach, fare in kinds:
            j = start[k]
            while x[i] - x[j] > reach:
                j += 1
            start[k] = j
            if j < i and (best is None or cost[j] + fare < best):
                best = cost[j] + fare
        cost[i] = best
    print(cost[b])


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
