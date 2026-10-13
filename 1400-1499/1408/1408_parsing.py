import sys

LETTERS = 26


def number(s, pos):
    """The number of digits starting at pos and the position after it."""
    end = pos
    while end < len(s) and s[end].isdigit():
        end += 1
    return int(s[pos:end]), end


def term(s, pos):
    """A term from pos: its coefficient, its powers and the position after it."""
    coef, powers = 1, [0] * LETTERS
    while True:
        if s[pos].isdigit():
            value, pos = number(s, pos)
            coef *= value
        else:
            var = ord(s[pos]) - ord("a")
            power, pos = 1, pos + 1
            if pos < len(s) and s[pos] == "^":
                power, pos = number(s, pos + 1)
            powers[var] += power
        if pos < len(s) and s[pos] == "*":
            pos += 1
        else:
            return coef, tuple(powers), pos


def parse(line):
    """A polynomial as a map from exponent tuples (a .. z) to coefficients."""
    s = "".join(line.split())  # spaces may stand anywhere
    poly, pos, sign = {}, 0, 1
    while pos < len(s):
        if s[pos] in "+-":
            sign, pos = (-1 if s[pos] == "-" else 1), pos + 1
        coef, powers, pos = term(s, pos)
        poly[powers] = poly.get(powers, 0) + sign * coef
    return poly


def main():
    lines = sys.stdin.read().split("\n")
    first, second = parse(lines[0]), parse(lines[1])
    product = {}
    for p, a in first.items():
        for q, b in second.items():
            key = tuple(x + y for x, y in zip(p, q))
            product[key] = product.get(key, 0) + a * b
    terms = [(key, c) for key, c in product.items() if c != 0]
    # by total degree, then by the powers of a, b, ... from the largest
    terms.sort(key=lambda t: (-sum(t[0]), [-e for e in t[0]]))
    out = []
    for k, (key, coef) in enumerate(terms):
        factors = [
            chr(ord("a") + v) + ("" if e == 1 else "^%d" % e) for v, e in enumerate(key) if e
        ]
        if abs(coef) != 1 or not factors:
            factors.insert(0, str(abs(coef)))
        body = "*".join(factors)
        if k == 0:
            out.append(("-" if coef < 0 else "") + body)
        else:
            out.append((" - " if coef < 0 else " + ") + body)
    print("".join(out) if out else "0")


main()
