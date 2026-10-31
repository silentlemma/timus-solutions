import sys
from bisect import bisect_left

MAX_VALUE = 5000


def main():
    stream = sys.stdin.buffer
    n = int(stream.readline())
    # the statement puts each value on its own line; retain only frequencies.
    counts = [0] * (MAX_VALUE + 1)
    for _ in range(n):
        counts[int(stream.readline())] += 1
    for value in range(1, MAX_VALUE + 1):
        counts[value] += counts[value - 1]
    stream.readline()
    k = int(stream.readline())
    print("\n".join(str(bisect_left(counts, int(stream.readline()))) for _ in range(k)))


main()
