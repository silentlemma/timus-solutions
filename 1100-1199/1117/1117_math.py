import sys


def trailing(x):
    return (x & -x).bit_length() - 1


def evens(n):
    """Sum over even e <= n of tz(e) - 1, that is sum over y <= n/2 of tz(y)."""
    m = n // 2
    return m - bin(m).count("1")


def main():
    i, j = sorted(map(int, sys.stdin.read().split()))
    # numbers run through the tree in order, so a node's height is the count of
    # trailing zeros; between k and k + 1 the even one is an ancestor of the
    # odd leaf, and the message waits one day per node in between
    inner = evens(j) - evens(i - 1)
    ends = sum(trailing(x) - 1 for x in {i, j} if x % 2 == 0)
    print(2 * inner - ends if i < j else 0)


main()
