import sys

KINDS = 3
# the input: lengths, prices, then N and the two stations, then positions
PRICES = KINDS
QUERY = 2 * KINDS
POSITIONS = QUERY + 3


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    length, price = data[:PRICES], data[PRICES:QUERY]
    n, a, b = data[QUERY:POSITIONS]
    x = [0, 0] + data[POSITIONS : POSITIONS + n - 1]
    a, b = min(a, b), max(a, b)
    # cost[i]: the cheapest way from a to i; it never decreases along the
    # line, so for every kind of ticket the farthest start in reach is best
    cost = [0] * (n + 1)
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
