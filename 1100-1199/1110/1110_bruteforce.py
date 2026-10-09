import sys


def main():
    n, m, y = map(int, sys.stdin.read().split())
    # only M candidates, each checked by fast modular power; a Y of M or more
    # is never a remainder
    roots = [x for x in range(m) if pow(x, n, m) == y]
    print(" ".join(map(str, roots)) if roots else -1)


main()
