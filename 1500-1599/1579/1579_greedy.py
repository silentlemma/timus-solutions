import sys


def main():
    words = iter(sys.stdin.buffer.read().split())
    n, r = int(next(words)), int(next(words))
    sizes = [int(next(words)) for _ in range(n)]
    # coats whose sizes lie within r of each other need different trips, so
    # the largest number of sizes in a window [x, x + r] is a lower bound
    trips, lo = 0, 0
    for hi in range(n):
        while sizes[hi] - sizes[lo] > r:
            lo += 1
        trips = max(trips, hi - lo + 1)
    # and it is enough: dealing the sorted coats round, the coat after coat i
    # in a trip is coat i + trips, which lies beyond that window
    out = [str(trips)]
    for t in range(trips):
        coats = range(t + 1, n + 1, trips)
        out.append("%d %s" % (len(coats), " ".join(map(str, coats))))
    sys.stdout.write("\n".join(out) + "\n")


main()
