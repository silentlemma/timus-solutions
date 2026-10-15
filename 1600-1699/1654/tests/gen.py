"""One test from a seed and a mode: a text without doubled letters with
pairs inserted (mode 1 short, mode 2 up to 200000 letters, mode 3 nested
pairs only, so that everything cancels). Inserted material is a balanced
block: every letter is later closed by the same letter, so it cancels."""

import random
import sys

LONGEST = 200000


def block(rng, letters, size):
    out, stack = [], []
    while len(out) + len(stack) < size or stack:
        if stack and (rng.random() < 0.5 or len(out) + len(stack) >= size):
            out.append(stack.pop())
        else:
            c = rng.choice(letters)
            out.append(c)
            stack.append(c)
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    letters = "abcdefghijklmnopqrstuvwxyz"[: rng.choice([2, 3, 26])]
    if mode == 3:
        print("".join(block(rng, letters, LONGEST)))
        return
    size = rng.randint(1, 20) if mode == 1 else LONGEST // 2
    base = [rng.choice(letters)]
    while len(base) < size:
        c = rng.choice(letters)
        if c != base[-1]:
            base.append(c)
    extra = rng.randint(0, 20) if mode == 1 else LONGEST - size
    out = []
    budget = extra
    for c in base + [None]:
        piece = rng.randint(0, budget) if c is not None else budget
        piece -= piece % 2
        out += block(rng, letters, piece)
        budget -= piece
        if c is not None:
            out.append(c)
    print("".join(out[:LONGEST]))


main()
