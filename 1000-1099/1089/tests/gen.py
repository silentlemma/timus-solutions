"""Deterministic dictionary and text modes:

SEED SIZE COUNT: original random mix; same-length words differ in at least
three places, so every typo has one correction.
all-typos SEED: 100 eight-letter words and 1000 correctable occurrences,
cycling through every dictionary word and substitution position.
near-misses SEED: 100 eight-letter words and 1000 uncorrectable words,
each differing from its source in the last two positions.
"""

import random
import sys

LETTERS = "abcdefghijklmnopqrstuvwxyz"
SHORTEST, LONGEST, LONGEST_TEXT_WORD = 3, 8, 16
LINE = 80
GAP = 3
SEPARATORS = [" ", " ", " ", ", ", ". ", "-", " (", ") ", "'", "  ", "; "]


def far(a, b):
    return len(a) != len(b) or sum(x != y for x, y in zip(a, b)) >= GAP


def boundary(mode, seed):
    rng = random.Random(seed)
    words = []
    while len(words) < 100:
        word = "".join(rng.choice(LETTERS) for _ in range(LONGEST))
        if all(sum(a != b for a, b in zip(word, d)) >= 5 for d in words):
            words.append(word)
    text = []
    for i in range(1000):
        word = words[i % len(words)]
        positions = [i // len(words) % LONGEST] if mode == "all-typos" else [6, 7]
        for pos in positions:
            word = word[:pos] + rng.choice(LETTERS.replace(word[pos], "")) + word[pos + 1 :]
        text.append(word)
    lines = [" ".join(text[i : i + 8]) for i in range(0, len(text), 8)]
    sys.stdout.buffer.write(("\n".join(words) + "\n#\n" + "\n".join(lines) + "\n").encode())


def main():
    if sys.argv[1] in ("all-typos", "near-misses"):
        boundary(sys.argv[1], int(sys.argv[2]))
        return
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
