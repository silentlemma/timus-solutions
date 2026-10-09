"""Random lines for the number reader: a seed and the number of pairs. About
half of the lines are numbers of every shape, the rest are numbers with a
character inserted, removed or replaced, using all characters 32-255."""

import random
import re
import sys
from fractions import Fraction

LONGEST_LINE = 100
LONGEST_OUTPUT = 200
MAX_DIGITS = 100
HIGHEST_CODE = 255
SPACE = 32
GRAMMAR = re.compile(r"[+-]?([0-9]+|\.[0-9]+|[0-9]+\.[0-9]+)([eE][+-]?[0-9]+)?")
FAR = 1000


def digits(rng, most):
    size = rng.randint(1, most)
    lead = "0" * rng.choice([0, 0, 0, rng.randint(1, size)])
    return (lead + "".join(rng.choice("0123456789") for _ in range(size)))[:size]


def number(rng):
    sign = rng.choice(["", "", "+", "-"])
    shape = rng.randrange(3)
    if shape == 0:
        body = digits(rng, rng.choice([3, 20, 60]))
    elif shape == 1:
        body = "." + digits(rng, rng.choice([3, 20, 60]))
    else:
        body = digits(rng, rng.choice([3, 20])) + "." + digits(rng, rng.choice([3, 20, 60]))
    text = sign + body
    if rng.random() < 0.6:
        exp = rng.choice([rng.randint(0, 9), rng.randint(0, 120), rng.randint(0, 10**30)])
        text += (
            rng.choice("eE")
            + rng.choice(["", "+", "-", "-"])
            + str(exp).zfill(rng.choice([1, 1, 5]))
        )
    return text


def output_length(s, n):
    m = GRAMMAR.fullmatch(s)
    if not m:
        return 0
    body = m.group(1)
    whole, _, frac = body.partition(".")
    mant = Fraction(int((whole + frac) or "0"), 10 ** len(frac))
    exp = int(m.group(2)[1:]) if m.group(2) else 0
    if mant == 0 or exp < -FAR:
        return n + 2
    if exp > FAR:
        return LONGEST_OUTPUT + 1
    value = int(mant * Fraction(10) ** exp)
    return len(str(value)) + n + 2


def mutate(rng, s):
    pos = rng.randint(0, len(s))
    char = chr(rng.randint(SPACE, HIGHEST_CODE))
    kind = rng.randrange(3)
    if kind == 0:
        return s[:pos] + char + s[pos:]
    if kind == 1 and s:
        pos = min(pos, len(s) - 1)
        return s[:pos] + s[pos + 1 :]
    pos = min(pos, len(s) - 1)
    return s[:pos] + char + s[pos + 1 :]


def main():
    seed, pairs = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    while len(lines) < 2 * pairs:
        s = number(rng)
        if rng.random() < 0.5:
            s = mutate(rng, s)
        n = rng.choice([0, rng.randint(0, 10), rng.randint(0, MAX_DIGITS)])
        if s == "#" or len(s) > LONGEST_LINE or output_length(s, n) > LONGEST_OUTPUT:
            continue
        lines += [s, str(n)]
    lines += ["#", "0"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
