import sys

HUNDREDTHS = 100
WHOLE = 100 * HUNDREDTHS


def hundredths(s):
    """A percentage with at most two decimals, in hundredths of a percent."""
    whole, _, fraction = s.partition(".")
    return int(whole or "0") * HUNDREDTHS + int((fraction + "00")[:2])


def main():
    p, q = map(hundredths, sys.stdin.read().split())
    # Stern-Brocot descent between 0/1 and 1/0: the first mediant inside
    # the open interval (p, q) / WHOLE has the smallest denominator
    left, right = (0, 1), (1, 0)
    while True:
        m, n = left[0] + right[0], left[1] + right[1]
        if m * WHOLE <= p * n:
            left = (m, n)
        elif m * WHOLE >= q * n:
            right = (m, n)
        else:
            print(n)
            return


main()
