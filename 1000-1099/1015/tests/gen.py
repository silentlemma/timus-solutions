"""Deterministic dice inputs; modes:

SEED N K: random rotations of K distinct kinds (the original mode).
tail SEED N K: one kind followed by K-1 new singleton kinds at the end.
blocks SEED N K: K contiguous, nearly equal groups with random orientations.
All modes require 1 <= K <= 30 and 1 <= N <= 100000.
The tail and blocks modes additionally require K <= N.
"""

import random
import sys

FACES = 6
# a quarter turn around the vertical axis and one around the left-right axis,
# as "new face at position i = old face at position TURN[i]"
TURNS = ((3, 5, 2, 1, 4, 0), (0, 1, 5, 2, 3, 4))


def rotations(die):
    seen, todo = {die}, [die]
    while todo:
        d = todo.pop()
        for turn in TURNS:
            r = tuple(d[i] for i in turn)
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return sorted(seen)


def main():
    args = sys.argv[1:]
    mode = args.pop(0) if args and args[0] in ("tail", "blocks") else "random"
    seed, n, kinds = (int(x) for x in args)
    if not 1 <= kinds <= 30 or not 1 <= n <= 100000:
        raise ValueError("require 1 <= K <= 30 and 1 <= N <= 100000")
    if mode != "random" and kinds > n:
        raise ValueError("tail and blocks require K <= N")
    rng = random.Random(seed)
    classes = []
    while len(classes) < kinds:
        die = list(range(1, FACES + 1))
        rng.shuffle(die)
        variants = rotations(tuple(die))
        if all(variants[0] != c[0] for c in classes):
            classes.append(variants)
    lines = [str(n)]
    for i in range(n):
        if mode == "tail":
            group = max(0, i - (n - kinds))
            die = rng.choice(classes[group])
        elif mode == "blocks":
            die = rng.choice(classes[i * kinds // n])
        else:
            die = rng.choice(rng.choice(classes))
        lines.append(" ".join(map(str, die)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
