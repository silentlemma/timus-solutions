"""Checker: "Irreducible" exactly when expected; otherwise factors in
parentheses, each written the canonical way, of degree at least 1, as
many as expected, whose product is the polynomial."""

import re
import sys

IRREDUCIBLE = "Irreducible"
TERM = re.compile(r"([+-]?)(\d*)(x(\d*))?")


def fail(reason):
    print(reason)
    sys.exit(1)


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
    return "".join(out)


def parse(text):
    """Coefficients from the highest power down, or None."""
    terms = {}
    pos = 0
    while pos < len(text):
        m = TERM.match(text, pos)
        if not m or m.end() == pos or (m.group(2) == "" and m.group(3) is None):
            return None
        sign = -1 if m.group(1) == "-" else 1
        size = int(m.group(2)) if m.group(2) else 1
        power = (int(m.group(4)) if m.group(4) else 1) if m.group(3) else 0
        if power in terms:
            return None
        terms[power] = sign * size
        pos = m.end()
    if not terms:
        return None
    deg = max(terms)
    return [terms.get(p, 0) for p in range(deg, -1, -1)]


def multiply(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] += x * y
    return out


def main():
    source, expected, output = sys.argv[1:4]
    a, b, c, d = (int(w) for w in open(source).read().split())
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if want == IRREDUCIBLE or got == IRREDUCIBLE:
        if want != got:
            fail("expected %r, got %r" % (want[:40], got[:40]))
        return
    if not (got.startswith("(") and got.endswith(")")):
        fail("not a product of factors in parentheses")
    pieces = got[1:-1].split(")(")
    product = [1]
    for piece in pieces:
        poly = parse(piece)
        if poly is None or len(poly) < 2 or show(poly) != piece:
            fail("factor %r is not written the canonical way" % piece)
        product = multiply(product, poly)
    if product != [1, a, b, c, d]:
        fail("the product is not the polynomial")
    if len(pieces) != want.count("("):
        fail("%d factors, expected %d" % (len(pieces), want.count("(")))


main()
