import sys
from itertools import accumulate

LOCKED = ord("*")
ZERO = ord("0")


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    states = b"".join(data[2:])[:n]
    # value[i] and locks[i]: the sum of values and the number of locked
    # buffers among the first i buffers
    value = [0, *accumulate(0 if c == LOCKED else c - ZERO for c in states)]
    locks = [0, *accumulate(c == LOCKED for c in states)]
    # the windows [left, left + k - 1] without locks; the first cheapest wins
    best, best_value = 0, 0
    for left in range(1, n - k + 2):
        right = left + k - 1
        if locks[right] != locks[left - 1]:
            continue
        v = value[right] - value[left - 1]
        if best == 0 or v < best_value:
            best, best_value = left, v
    print(best)


main()
