import sys

BASE = 10
TOP = 10**18  # more than 10^18 ones are counted below this floor


def ones(x):
    """The number of digits 1 in the numbers from 1 to x: at each place p,
    every full block of 10 p numbers holds p ones there, and the last part
    adds p, the rest past the 1, or nothing, as its digit is above, at or
    below 1."""
    total, p = 0, 1
    while p <= x:
        high, digit, low = x // (p * BASE), x // p % BASE, x % p
        total += high * p
        if digit > 1:
            total += p
        elif digit == 1:
            total += low + 1
        p *= BASE
    return total


def main():
    k = int(sys.stdin.read())
    # the floor where the k-th one was counted is the first x with ones(x) >= k
    lo, hi = 1, TOP
    while lo < hi:
        mid = (lo + hi) // 2
        if ones(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    print(lo if ones(lo) == k else "Petr lies")


main()
