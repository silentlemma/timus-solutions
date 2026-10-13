import sys
from fractions import Fraction

STEPS = 100  # halvings of the search interval: far below the 1e-6 asked
QUARTIC = 4


def value(poly, x):
    s = 0
    for c in poly:
        s = s * x + c
    return s


def derivative(poly):
    n = len(poly) - 1
    return [c * (n - i) for i, c in enumerate(poly[:-1])]


def sign(v):
    return (v > 0) - (v < 0)


def sign_roots(poly, lo, hi):
    """Points where poly changes sign inside (lo, hi), found exactly.

    Between two neighbouring sign changes of the derivative the polynomial
    is monotone, so each piece holds at most one sign change."""
    if len(poly) < 2:
        return []
    cuts = [lo] + sign_roots(derivative(poly), lo, hi) + [hi]
    found = []
    for a, b in zip(cuts, cuts[1:]):
        sa, sb = sign(value(poly, a)), sign(value(poly, b))
        if sa == 0 or sb == 0 or sa == sb:
            continue
        for _ in range(STEPS):
            mid = (a + b) / 2
            sm = sign(value(poly, mid))
            if sm == 0:
                a = b = mid
                break
            if sm == sa:
                a = mid
            else:
                b = mid
        found.append((a + b) / 2)
    return found


def divisors(v):
    v = abs(v)
    return [d for d in range(1, v + 1) if v % d == 0]


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    n = data[0]
    poly = data[1 : n + 2]  # the leading coefficient first
    roots = []

    # rational roots p/q, with p dividing the constant term and q the
    # leading one; dividing by (q x - p) keeps integer coefficients
    while len(poly) > 1 and poly[-1] == 0:
        roots.append(Fraction(0))
        poly = poly[:-1]
    changed = True
    while changed and len(poly) > 1:
        changed = False
        for q in divisors(poly[0]):
            for p in divisors(poly[-1]):
                for p in (p, -p):
                    if value(poly, Fraction(p, q)) == 0:
                        out = [poly[0] // q]
                        for c in poly[1:-1]:
                            out.append((c + p * out[-1]) // q)
                        poly = out
                        roots.append(Fraction(p, q))
                        changed = True
                        break
                if changed:
                    break
            if changed:
                break

    # what is left has no rational roots; a repeated irrational root would
    # need its quadratic twice, so only c (x^2 + b x + d)^2 can repeat
    if len(poly) == QUARTIC + 1:
        s3, s2, s1, s0 = (Fraction(c, poly[0]) for c in poly[1:])
        b = s3 / 2
        d = (s2 - b * b) / 2
        if 2 * b * d == s1 and d * d == s0:
            edge = 1 + abs(b) + abs(d)
            for r in sign_roots([1, b, d], -edge, edge):
                roots += [r, r]
            poly = [1]

    bound = 1 + max((abs(Fraction(c, poly[0])) for c in poly[1:]), default=0)
    roots += sign_roots(poly, -bound, bound)
    print("\n".join("%.10f" % float(r) for r in sorted(roots)))


main()
