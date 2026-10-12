import sys
from itertools import accumulate


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # before[i] is the sum of the first i readings
    before = [0, *accumulate(map(int, data[1 : n + 1]))]
    q = int(data[n + 1]) if len(data) > n + 1 else 0
    ends = list(map(int, data[n + 2 : n + 2 + 2 * q]))
    print("\n".join(str(before[j] - before[i - 1]) for i, j in zip(ends[::2], ends[1::2])))


main()
