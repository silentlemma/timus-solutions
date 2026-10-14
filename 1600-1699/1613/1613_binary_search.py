import sys
from bisect import bisect_left

QUERY = 3  # numbers in a query


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # (passengers, city) pairs in order: the cities with one count are
    # consecutive and sorted by number
    pairs = sorted(zip(map(int, data[1 : n + 1]), range(1, n + 1)))
    q = int(data[n + 1])
    out = []
    for i in range(q):
        base = n + 2 + QUERY * i
        lo, hi, x = int(data[base]), int(data[base + 1]), int(data[base + 2])
        # the first city with count x and number at least lo
        k = bisect_left(pairs, (x, lo))
        out.append("1" if k < n and pairs[k][0] == x and pairs[k][1] <= hi else "0")
    print("".join(out))


main()
