import sys

TOP = 10  # the highest vote
HALVES = 20  # a rating counts in half tenths


def tenths(text):
    whole, _, part = text.partition(".")
    return int(whole) * 10 + int((part + "0")[0])


def main():
    xs, ys, ns = sys.stdin.read().split()
    x, y, n = tenths(xs), tenths(ys), int(ns)
    # n votes from 1 to 10 show x when (2x - 1) n <= 20 sum < (2x + 1) n,
    # and the worst case is the largest such sum, and there may be none at all
    total = min(TOP * n, ((2 * x + 1) * n - 1) // HALVES)
    least = max(n, -(-(2 * x - 1) * n // HALVES))
    # k votes of 1 show at most y when 20 (total + k) < (2y + 1)(n + k)
    excess = HALVES * total - (2 * y + 1) * n
    step = 2 * y + 1 - HALVES
    if least > total or (excess >= 0 and step <= 0):
        print("Impossible")
    elif excess < 0:
        print(0)
    else:
        print(excess // step + 1)


main()
