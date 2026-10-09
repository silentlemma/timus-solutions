"""Random dialogues: a seed, the number of lines, their total length and the
share of lines spoiled by one changed, inserted or removed letter in
percent."""

import random
import sys

WORDS = ["out", "output", "puton", "in", "input", "one"]
LETTERS = "inoptue"
PERCENT = 100


def main():
    seed, n, total, spoiled = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = []
    used = 0
    for i in range(n):
        # one letter is kept in reserve for a spoiling insertion
        target = (total - used) // (n - i) - 1
        words = []
        length = 0
        while True:
            fits = [w for w in WORDS if length + len(w) <= target]
            if not fits:
                break
            words.append(rng.choice(fits))
            length += len(words[-1])
        s = "".join(words) or rng.choice(WORDS)
        if rng.randrange(PERCENT) < spoiled:
            pos = rng.randrange(len(s))
            kind = rng.randrange(3)
            if kind == 0:
                s = s[:pos] + rng.choice(LETTERS) + s[pos + 1 :]
            elif kind == 1:
                s = s[:pos] + rng.choice(LETTERS) + s[pos:]
            elif len(s) > 1:
                s = s[:pos] + s[pos + 1 :]
        lines.append(s)
        used += len(s)
    sys.stdout.write("\n".join([str(n)] + lines) + "\n")


if __name__ == "__main__":
    main()
