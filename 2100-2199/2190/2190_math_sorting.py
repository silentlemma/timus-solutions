import sys
from functools import cmp_to_key
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    s = data[1:n + 1]
    p = data[n + 1:2 * n + 1]
    g = 0
    for value in p:
        g = gcd(g, value)
    q = [value // g for value in p]
    # The heaps become k * q for an integer k >= 1, and the cost
    # sum |s - k q| = sum q |s / q - k| is convex in k with its real minimum
    # at the median of the ratios s / q weighted by q.
    order = sorted(range(n), key=cmp_to_key(lambda i, j: s[i] * q[j] - s[j] * q[i]))
    total = sum(q)
    weight = 0
    median = order[-1]
    for i in order:
        weight += q[i]
        if 2 * weight >= total:
            median = i
            break
    low = s[median] // q[median]

    def cost(k):
        return sum(abs(a - k * b) for a, b in zip(s, q))

    print(min(cost(k) for k in (low, low + 1) if k >= 1))


main()
