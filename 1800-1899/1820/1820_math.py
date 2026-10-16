import sys

SIDES = 2


def main():
    n, k = map(int, sys.stdin.read().split())
    # every minute fries at most k of the 2n sides, and one steak takes
    # two minutes on its own; rotating sides cyclically reaches both bounds
    print(max(SIDES, (SIDES * n + k - 1) // k))


main()
