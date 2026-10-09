"""A random dictionary and text: a seed, the number of dictionary words
and the number of words in the text. Dictionary words of one length
differ in at least three places, so every typo has one correction."""

import random
import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
SHORTEST, LONGEST, LONGEST_TEXT_WORD = 3, 8, 16
LINE = 80
GAP = 3
SEPARATORS = [" ", " ", " ", ", ", ". ", "-", " (", ") ", "'", "  ", "; "]


def far(a, b):
    return len(a) != len(b) or sum(x != y for x, y in zip(a, b)) >= GAP


def main():
    seed, size, count = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    words = []
    while len(words) < size:
        w = "".join(rng.choice(LETTERS) for _ in range(rng.randint(SHORTEST, LONGEST)))
        if all(far(w, d) for d in words):
            words.append(w)
    text = []
    for _ in range(count):
        kind = rng.randrange(3)
        w = rng.choice(words)
        if kind == 1:
            i = rng.randrange(len(w))
            w = w[:i] + rng.choice(LETTERS.replace(w[i], "")) + w[i + 1 :]
        elif kind == 2:
            w = "".join(rng.choice(LETTERS) for _ in range(rng.randint(1, LONGEST_TEXT_WORD)))
        text.append(w)
    lines, line = [], ""
    for w in text:
        piece = w + rng.choice(SEPARATORS)
        if len(line) + len(piece) > LINE:
            lines.append(line.rstrip())
            line = ""
        line += piece
    lines.append(line.rstrip())
    sys.stdout.write("\n".join(words) + "\n#\n" + "\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
