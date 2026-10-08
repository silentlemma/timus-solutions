"""Random dice; a seed, the number of dice and the number of distinct dice
they are rotations of (at most 30)."""

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
    seed, n, kinds = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    classes = []
    while len(classes) < kinds:
        die = list(range(1, FACES + 1))
        rng.shuffle(die)
        variants = rotations(tuple(die))
        if all(variants[0] != c[0] for c in classes):
            classes.append(variants)
    lines = [str(n)]
    for _ in range(n):
        lines.append(" ".join(map(str, rng.choice(rng.choice(classes)))))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
