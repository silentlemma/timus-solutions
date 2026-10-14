import math
import sys

TOTAL = 1000
HALF = 0.5


def main():
    k1, k2, k3 = (float(v) for v in sys.stdin.read().split())
    # betting in proportion to 1 / k on every outcome pays the same whatever
    # happens, and any other split pays less on some outcome
    payout = TOTAL / (1 / k1 + 1 / k2 + 1 / k3)
    print(math.floor(payout + HALF))


main()
