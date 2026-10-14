import sys

BASE = 10


def scaled(text, d):
    """The decimal text times 10^d, as an integer."""
    whole, _, frac = text.partition(".")
    frac = (frac + "0" * d)[:d]
    return int(whole or "0") * BASE**d + int(frac or "0")


def main():
    data = sys.stdin.read().split()
    d, n = int(data[0]), int(data[1])
    one = BASE**d
    # only the fractional parts matter, and a whole number fits any group
    values = sorted({scaled(t, d) % one for t in data[2 : 2 + n]} - {0})
    den = 2 * one
    # an average v (times 10^d) over q goblins comes from a total p when
    # (2v - 1) q <= den p < (2v + 1) q; q = 10^d always works, as the
    # interval is then at least 1 long
    for q in range(1, one + 1):
        for i, v in enumerate(values):
            low = -(-(2 * v - 1) * q // den)  # the smallest total allowed
            if low * den >= (2 * v + 1) * q:
                # the average that failed is likely to fail again: try it first
                values.insert(0, values.pop(i))
                break
        else:
            print(q)
            return


main()
