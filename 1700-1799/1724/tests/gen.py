"""One test from a seed and a mode: mode 1 a short string with every
substring asked, mode 2 a random string of 100000 letters, mode 3 a
balanced string of 100000 letters asked mostly about balanced pieces,
mode 4 50000 nested pairs, mode 5 a balanced string with a few letters
changed, mode 6 100000 opening letters, mode 7 100000 closing letters,
mode 8 50000 adjacent random pairs with repeated long boundary queries."""

import random
import sys

OPEN = "ACGT"
LONGEST = 100000
QUERIES = 50000
SHORT = 30
CHANGES = 20


def balanced(rng, size):
    out, stack = [], []
    while len(out) < size:
        if stack and (rng.random() < 0.5 or len(out) + len(stack) >= size):
            out.append(stack.pop().lower())
        else:
            stack.append(rng.choice(OPEN))
            out.append(stack[-1])
    return out


def pieces(rng, dna, count):
    partner, stack = {}, []
    for i, c in enumerate(dna):
        if c in OPEN:
            stack.append(i)
        elif stack and dna[stack[-1]] == c.upper():
            partner[stack.pop()] = i
    starts = sorted(partner)
    asked = []
    for _ in range(count):
        if rng.random() < 0.5 or not starts:
            left = rng.randint(1, len(dna))
            asked.append((left, rng.randint(left, len(dna))))
            continue
        i = rng.choice(starts)
        right = partner[i]
        while right + 1 in partner and rng.random() < 0.7:
            right = partner[right + 1]
        asked.append((i + 1, right + 1))
    return asked


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        dna = [rng.choice("AaCc") for _ in range(rng.randint(1, SHORT))]
        asked = [(l, r) for l in range(1, len(dna) + 1) for r in range(l, len(dna) + 1)]
    elif mode in (6, 7, 8):
        if mode == 8:
            dna = []
            for _ in range(LONGEST // 2):
                c = rng.choice(OPEN)
                dna.extend((c, c.lower()))
            asked = [(rng.randint(1, 4), LONGEST - rng.randrange(4)) for _ in range(QUERIES)]
        else:
            alphabet = OPEN if mode == 6 else OPEN.lower()
            dna = [rng.choice(alphabet) for _ in range(LONGEST)]
            asked = []
            for _ in range(QUERIES):
                left = rng.randint(1, LONGEST)
                asked.append((left, rng.randint(left, LONGEST)))
        asked[:4] = [(1, LONGEST), (1, 1), (LONGEST, LONGEST), (1, LONGEST - 1)]
    else:
        if mode == 2:
            dna = [rng.choice("ACGTacgt") for _ in range(LONGEST)]
        elif mode == 4:
            half = [rng.choice(OPEN) for _ in range(LONGEST // 2)]
            dna = half + [c.lower() for c in reversed(half)]
        else:
            dna = balanced(rng, LONGEST)
        if mode == 5:
            for _ in range(CHANGES):
                dna[rng.randrange(LONGEST)] = rng.choice("ACGTacgt")
        asked = pieces(rng, dna, QUERIES)
    print("".join(dna))
    print(len(asked))
    print("\n".join("%d %d" % p for p in asked))


main()
