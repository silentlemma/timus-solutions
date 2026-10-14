"""One test from a seed and a mode: an expression of up to 10000 characters.
Mode 1 nests a starred letter in about 5000 brackets, mode 2 nests 0* the
same way under letters, mode 3 is a random expression whose stars only
apply to sets without non-empty words unless a 0 kills them, mode 4 is a
random expression with letters under some stars, mode 5 chains 2000
choices of two letters."""

import random
import sys

LONGEST = 10000
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def random_expression(rng, budget, safe):
    """A random expression of about budget characters; when safe, every star
    applies to 0 or to a set holding only the empty word, or sits next to a
    0 in a concatenation."""
    if budget <= 1:
        return rng.choice(LETTERS + "0")
    parts = []
    while budget > 0:
        size = rng.randint(1, max(1, budget // 2))
        budget -= size + 1
        kind = rng.random()
        if kind < 0.3 or size < 4:
            part = rng.choice(LETTERS)
        elif kind < 0.5:
            inner = random_expression(rng, size - 3, safe)
            if safe:
                part = "(" + inner + ")*0"
            else:
                part = "(" + inner + ")*"
        elif kind < 0.6:
            part = "(0" + "*" * rng.randint(1, 3) + ")*"
        else:
            part = "(" + random_expression(rng, size - 2, safe) + ")"
        parts.append(part)
    glue = "|" if rng.random() < 0.5 else ""
    return glue.join(parts)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    depth = (LONGEST - 4) // 2
    if mode == 1:
        text = "(" * depth + rng.choice(LETTERS) + "*" + ")" * depth
    elif mode == 2:
        text = "(" * depth + "0*" + ")" * depth
        text += "ab"
    elif mode == 5:
        text = "(a|b)" * (LONGEST // len("(a|b)"))
    else:
        text = random_expression(rng, LONGEST, mode == 3)
        while len(text) > LONGEST:
            text = random_expression(rng, LONGEST, mode == 3)
    print(text)


main()
