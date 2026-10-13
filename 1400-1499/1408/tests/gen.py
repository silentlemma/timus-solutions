"""Modes:
dense: two 100-character lines over disjoint alphabets, giving 961 product terms.
random SEED: two seeded polynomials with mixed signs, coefficients and powers.
"""

import itertools
import random
import sys


def dense():
    lines = []
    for alphabet in ("abcdefghijklm", "nopqrstuvwxyz"):
        terms = list(alphabet)
        pairs = itertools.combinations_with_replacement(alphabet, 2)
        terms.extend(a + "*" + b for a, b in itertools.islice(pairs, 18))
        lines.append("+".join(terms).ljust(100))
    return lines


def polynomial(rng):
    terms = []
    for _ in range(7):
        factors = []
        for _ in range(rng.randrange(3)):
            letter, power = rng.choice("abmnxyz"), rng.randrange(5)
            factors.append(letter if power == 1 else f"{letter}^{power}")
        if not factors or rng.randrange(2):
            coefficient = rng.choice((0, 1, 1, 2, 3, 7, 100))
            factors.insert(0, "0" * rng.randrange(2) + str(coefficient))
        sign = rng.choice(("+", "-")) if terms else rng.choice(("", "-"))
        term = sign + "*".join(factors)
        if len("".join(terms)) + len(term) <= 88:
            terms.append(term)
    line = "".join(terms)
    for _ in range(rng.randrange(13)):
        pos = rng.randrange(len(line) + 1)
        line = line[:pos] + " " + line[pos:]
    return line


def main():
    if sys.argv[1:] == ["dense"]:
        lines = dense()
    elif len(sys.argv) == 3 and sys.argv[1] == "random":
        rng = random.Random(int(sys.argv[2]))
        lines = [polynomial(rng), polynomial(rng)]
    else:
        raise ValueError("expected: dense | random SEED")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
