"""Deterministic modes:

SEED N TOTAL SPOILED: random dialogues, with SPOILED percent of lines edited.
shortest: one valid line of exactly four million letters, using only 'in'.
bad-prefix: four million letters, an invalid first letter and a valid suffix.
boundary SEED PAIRS: random dialogues paired with swaps across word boundaries.
"""

import random
import sys

WORDS = ["out", "output", "puton", "in", "input", "one"]
LETTERS = "inoptue"
PERCENT = 100


def main():
    if sys.argv[1] == "shortest":
        sys.stdout.buffer.write(b"1\n" + b"in" * 2_000_000 + b"\n")
        return
    if sys.argv[1] == "bad-prefix":
        sys.stdout.buffer.write(b"1\n" + b"xone" + b"in" * 1_999_998 + b"\n")
        return
    if sys.argv[1] == "boundary":
        seed, pairs = map(int, sys.argv[2:4])
        if not 1 <= pairs <= 500:
            raise ValueError("PAIRS must be in 1..500")
        rng = random.Random(seed)
        lines = []
        for _ in range(pairs):
            words = [rng.choice(WORDS) for _ in range(rng.randint(10, 50))]
            line = "".join(words)
            cuts = []
            pos = 0
            for word in words[:-1]:
                pos += len(word)
                if line[pos - 1] != line[pos]:
                    cuts.append(pos)
            cut = rng.choice(cuts)
            swapped = line[:cut - 1] + line[cut] + line[cut - 1] + line[cut + 1:]
            lines.extend((line, swapped))
        sys.stdout.buffer.write(("\n".join([str(len(lines))] + lines) + "\n").encode("ascii"))
        return
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
