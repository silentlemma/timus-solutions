import sys

PERIOD = 6  # the simple pattern fails exactly when n mod 6 is 2


def even_rows(n):
    """The row of the queen in each column 1 ... n for even n; the main
    diagonal stays free."""
    half = n // 2
    if n % PERIOD != 2:
        # the even rows in the left half, the odd rows in the right half
        return [2 * i for i in range(1, half + 1)] + [2 * i - 1 for i in range(1, half + 1)]
    rows = [0] * n
    for i in range(1, half + 1):
        shift = (2 * (i - 1) + half - 1) % n
        rows[i - 1] = 1 + shift
        rows[n - i] = n - shift
    return rows


def main():
    n = int(sys.stdin.read())
    # an odd board is an even one plus the free corner (n, n)
    rows = even_rows(n) if n % 2 == 0 else even_rows(n - 1) + [n]
    print("\n".join("%d %d" % (col, row) for col, row in enumerate(rows, 1)))


main()
