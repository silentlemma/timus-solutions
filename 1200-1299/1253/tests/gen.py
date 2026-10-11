"""Templates: a seed, a mode and two numbers a and b. Mode 1 makes a
random templates that only refer to later ones, each up to b characters
with spaces and line breaks; mode 2 makes a chain where each of a
templates refers ten times to the next and the last is one letter, with
b more letters in the first, so the text has 10^a + b characters; mode 3
is mode 1 with one reference back to the first template, a cycle."""

import random
import string
import sys

REFS = 10
CHAIN = 10
LETTERS = string.ascii_letters + string.digits + ".,!? "


def template(rng, i, n, size):
    parts = []
    for _ in range(rng.randint(0, size)):
        r = rng.random()
        if r < 0.03 and i < n:
            parts.append("*%d" % rng.randint(i + 1, n))
        elif r < 0.08:
            parts.append("\n")
        else:
            parts.append(rng.choice(LETTERS))
    text = "".join(parts)
    while text.count("*") > REFS:
        text = text[text.index("*") + 2 :]
    return text


def main():
    seed, mode, a, b = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 2:
        texts = ["*%d" % (k + 1) * CHAIN for k in range(1, a + 1)] + ["a"]
        texts[0] += "b" * b
    else:
        texts = [template(rng, i, a, b) for i in range(1, a + 1)]
        if mode == 3:
            texts[-1] += "*1"
    lines = [str(len(texts))] + [t + "#" for t in texts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
