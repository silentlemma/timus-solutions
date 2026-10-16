import sys
from bisect import bisect_right

LIMIT = 10 ** 18
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
MOST = 64


def main():
    # the smallest number with a given set of exponents puts the largest
    # exponents on the smallest primes, so only numbers 2^a 3^b 5^c ...
    # with a >= b >= c >= ... can be answers
    found = []
    stack = [(0, MOST, 1, 1)]
    while stack:
        index, cap, value, divisors = stack.pop()
        found.append((value, divisors))
        if index == len(PRIMES):
            continue
        p = PRIMES[index]
        for e in range(1, cap + 1):
            if value > LIMIT // p:
                break
            value *= p
            stack.append((index + 1, e, value, divisors * (e + 1)))
    found.sort()
    values, best = [], []
    top = (0, 0)
    for value, divisors in found:
        if divisors > top[1]:
            top = (value, divisors)
        values.append(value)
        best.append(top)
    data = sys.stdin.read().split()
    out = []
    for w in data[1:int(data[0]) + 1]:
        value, divisors = best[bisect_right(values, int(w)) - 1]
        out.append("%d %d" % (value, divisors))
    print("\n".join(out))


main()
