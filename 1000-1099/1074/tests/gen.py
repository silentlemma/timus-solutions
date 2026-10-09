"""Modes (all random choices are seeded):

SEED PAIRS: original mixed random lines; about half are mutated numbers,
    using all characters 32-255.
precision SEED: one long random decimal at every precision from 0 to 100.
cancel SEED PAIRS: 100-character mantissas shifted across their first or
    last significant digit, with leading zeros and random requested precision.
suffix SEED PAIRS: 100-character lines with a huge exponent followed by an
    illegal final character; valid records are interleaved to check recovery.
empty: only the terminating marker, with no number/precision pairs.
"""

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


def focused(mode, seed, pairs):
    rng = random.Random(seed)
    lines = []
    if mode == "precision":
        # Leading zeros exercise sign removal; sparse final digits exercise
        # truncation at the end of the mantissa.
        s = "-0." + "0" * 5 + "".join(rng.choice("0123456789") for _ in range(83))
        s += "001009e-4"
        for n in range(MAX_DIGITS + 1):
            lines += [s, str(n)]
    elif mode == "cancel":
        for i in range(pairs):
            lead = rng.randint(1, 65)
            sign = rng.choice(["", "+", "-"])
            # 1-character point and 4-character exponent leave 95-sign digits.
            width = LONGEST_LINE - len(sign) - 5
            body = "0" * lead + rng.choice("123456789")
            body += "".join(rng.choice("0123456789") for _ in range(width - len(body)))
            split = rng.randint(1, width - 1)
            if i % 2:
                point = lead + rng.choice([-1, 0, 1])
            else:
                point = width + rng.choice([-1, 0, 1])
            exp = point - split
            s = sign + body[:split] + "." + body[split:] + "e" + f"{exp:+03d}"
            n = rng.choice([0, 1, 100, rng.randint(0, MAX_DIGITS)])
            lines += [s, str(n)]
    elif mode == "suffix":
        for i in range(pairs):
            prefix = rng.choice(["0e+", "-0E-", "7e-", "-.1E-"])
            suffix = rng.choice(["+", "-", ".", "e", "E", " ", "#", "_", "\x85", "\xff"])
            s = prefix + "".join(rng.choice("123456789") for _ in range(99 - len(prefix)))
            lines += [s + suffix, str(rng.randint(0, MAX_DIGITS))]
            # Check that rejection consumes exactly one pair.
            lines += [f"-{i + 1}.25e-1", str(rng.randint(0, 6))]
    else:
        raise ValueError("unknown mode: " + mode)
    sys.stdout.write("\n".join(lines + ["#"]) + "\n")


def main():
    if sys.argv[1] == "empty":
        sys.stdout.write("#\n")
        return
    if sys.argv[1] in ("precision", "cancel", "suffix"):
        mode = sys.argv[1]
        seed = int(sys.argv[2])
        pairs = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        focused(mode, seed, pairs)
        return
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
