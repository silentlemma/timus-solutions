import sys

DIGITS = 6  # the input has at most six digits after the point


def scaled(token):
    """The number times 10^6 as an exact integer."""
    sign = -1 if token.startswith("-") else 1
    whole, _, frac = token.lstrip("+-").partition(".")
    frac = (frac + "0" * DIGITS)[:DIGITS]
    return sign * (int(whole or "0") * 10**DIGITS + int(frac))


def main():
    ex, ey, tx, ty, ax, ay, bx, by = (scaled(t) for t in sys.stdin.read().split())
    # mirror from A along s; the eye and the target relative to A
    sx, sy = bx - ax, by - ay
    ex, ey, tx, ty = ex - ax, ey - ay, tx - ax, ty - ay
    # heights above the mirror line (times |s|), both on one side
    he, ht = sx * ey - sy * ex, sx * ty - sy * tx
    if (he > 0) != (ht > 0):
        print("INVISIBLE")
        return
    # the ray to the target's image meets the line at the projections
    # weighted by the heights: u = (pe * ht + pt * he) / ((he + ht) |s|^2)
    pe, pt = sx * ex + sy * ey, sx * tx + sy * ty
    num, den = pe * ht + pt * he, (he + ht) * (sx * sx + sy * sy)
    if den < 0:
        num, den = -num, -den
    print("VISIBLE" if 0 <= num <= den else "INVISIBLE")


main()
