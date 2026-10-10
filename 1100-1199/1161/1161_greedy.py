import math
import sys


def main():
    tok = list(map(int, sys.stdin.read().split()))
    weights = sorted(tok[1 : 1 + tok[0]], reverse=True)
    # each collision takes a square root of the product, so the heaviest
    # stripies should meet first and be rooted the most times
    total = float(weights[0])
    for w in weights[1:]:
        total = 2 * math.sqrt(total * w)
    print("%.2f" % total)


main()
