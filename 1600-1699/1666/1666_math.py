import math
import sys

QUARTIC = 5  # coefficients of a degree-4 polynomial
DISCRIMINANT = 4  # t^2 - at + e has discriminant a^2 - 4e


def divisors(v):
    """The positive and negative divisors of v != 0."""
    v = abs(v)
    out = []
    d = 1
    while d * d <= v:
        if v % d == 0:
            out += [d, -d, v // d, -(v // d)]
        d += 1
    return out


def value(poly, x):
    result = 0
    for c in poly:
        result = result * x + c
    return result


def root(poly):
    """An integer root of a monic polynomial, or None: it divides the
    constant term."""
    if poly[-1] == 0:
        return 0
    for r in divisors(poly[-1]):
        if value(poly, r) == 0:
            return r
    return None


def quadratics(poly):
    """Two monic quadratics whose product is the monic quartic, or None:
    (x^2 + px + q)(x^2 + rx + s) with qs = d, p + r = a, q + s + pr = b,
    ps + qr = c."""
    _, a, b, c, d = poly
    for q in divisors(d):
        s = d // q
        if q != s:
            if (c - a * q) % (s - q):
                continue
            p = (c - a * q) // (s - q)
        else:
            # then p and r are the roots of t^2 - at + (b - 2q)
            disc = a * a - DISCRIMINANT * (b - 2 * q)
            if disc < 0 or math.isqrt(disc) ** 2 != disc or (a + math.isqrt(disc)) % 2:
                continue
            p = (a + math.isqrt(disc)) // 2
        r = a - p
        if q + s + p * r == b and p * s + q * r == c:
            return [1, p, q], [1, r, s]
    return None


def show(poly):
    deg = len(poly) - 1
    out = []
    for i, c in enumerate(poly):
        if c == 0:
            continue
        power = deg - i
        sign = "-" if c < 0 else ("+" if out else "")
        size = "" if abs(c) == 1 and power > 0 else str(abs(c))
        x = "" if power == 0 else "x" if power == 1 else "x%d" % power
        out.append(sign + size + x)
    return "(" + "".join(out) + ")"


def main():
    a, b, c, d = (int(w) for w in sys.stdin.read().split())
    poly = [1, a, b, c, d]
    factors = []
    while len(poly) > 2:
        r = root(poly)
        if r is None:
            break
        factors.append([1, -r])
        quotient = [1]
        for coef in poly[1:-1]:
            quotient.append(coef + r * quotient[-1])
        poly = quotient
    if len(poly) == QUARTIC:
        split = quadratics(poly)
        if split is None:
            print("Irreducible")
            return
        factors += list(split)
    elif len(poly) > 1:
        factors.append(poly)
    print("".join(show(f) for f in factors))


main()
