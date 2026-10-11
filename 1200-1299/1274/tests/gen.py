"""Two fractions and an operation: a seed and a mode. Mode 1 draws any
fractions within the limits, mode 2 small ones that are often reducible,
mode 3 parts near 30000. Only cases whose result stays within the limits
are kept."""

import random
import sys
from fractions import Fraction

TOP = 30000


def show(f):
    sign = "-" if f < 0 else ""
    whole, rest = divmod(abs(f.numerator), f.denominator)
    if not rest:
        return "%s%d" % (sign, whole)
    return "%s%s%d/%d" % (sign, "%d " % whole if whole else "", rest, f.denominator)


def fraction(rng, mode):
    top = {1: TOP, 2: 12, 3: TOP}[mode]
    den = rng.randint(TOP - 100, TOP) if mode == 3 else rng.randint(1, top)
    num = rng.randint(0, den - 1)
    whole = rng.randint(0, top) if rng.random() < 0.7 else 0
    sign = rng.choice([1, -1])
    # written as the input allows: possibly reducible, never "0 1/2"
    text = "-" if sign < 0 and (whole or num) else ""
    if num:
        text += ("%d " % whole if whole else "") + "%d/%d" % (num, den)
    else:
        text += "%d" % whole
    return text, sign * (whole + Fraction(num, den))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        (ta, a), (tb, b) = fraction(rng, mode), fraction(rng, mode)
        op = rng.choice("+-*/")
        if op == "/" and b == 0:
            continue
        r = {"+": a + b, "-": a - b, "*": a * b, "/": a / b if b else 0}[op]
        if abs(r) < TOP + 1 and r.denominator <= TOP:
            break
    sys.stdout.write("%s\n%s\n%s\n" % (ta, op, tb))


if __name__ == "__main__":
    main()
