import sys
from math import lcm


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, p = data[0], [0] + data[1 : 1 + data[0]]
    # P^k is the identity exactly when k is a multiple of every cycle length:
    # the order is their least common multiple
    seen, order = [False] * (n + 1), 1
    for i in range(1, n + 1):
        length, j = 0, i
        while not seen[j]:
            seen[j], j, length = True, p[j], length + 1
        if length:
            order = lcm(order, length)
    print(order)


main()
