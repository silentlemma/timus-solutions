"""One cut box from a seed and a mode: mode 1 a small random grid, 2 the
most pieces with long sections, 3 the most pieces as equal unit cubes,
4 a single layer, 5 a single row, 6 one piece, 7 the most pieces with
sections of lengths 1 and 2, so that many pieces have equal sides.
Every piece is listed in a random turn, in random order."""

import random
import sys

FACES = "FBDULR"
LIMIT = 1000
SIDE = 10


def rotations():
    turns = ((4, 5, 2, 3, 1, 0), (0, 1, 4, 5, 3, 2))
    seen = {tuple(range(len(FACES)))}
    todo = list(seen)
    while todo:
        p = todo.pop()
        for q in turns:
            r = tuple(p[q[k]] for k in range(len(FACES)))
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return sorted(seen)


def split(rng, total, parts):
    cuts = sorted(rng.sample(range(1, total), parts - 1))
    return [b - a for a, b in zip([0] + cuts, cuts + [total])]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        counts = [rng.randint(1, 3) for _ in range(3)]
        cuts = [split(rng, rng.randint(c, 9), c) for c in counts]
    elif mode == 2:
        cuts = [split(rng, rng.randint(LIMIT // 2, LIMIT), SIDE) for _ in range(3)]
    elif mode == 3:
        cuts = [[1] * SIDE for _ in range(3)]
    elif mode == 4:
        cuts = [[rng.randint(1, LIMIT)], split(rng, LIMIT, 25), split(rng, LIMIT, 40)]
        rng.shuffle(cuts)
    elif mode == 5:
        cuts = [[rng.randint(1, LIMIT)], [rng.randint(1, LIMIT)], [1] * LIMIT]
        rng.shuffle(cuts)
    elif mode == 6:
        cuts = [[rng.randint(1, LIMIT)] for _ in range(3)]
    else:
        cuts = [[rng.randint(1, 2) for _ in range(SIDE)] for _ in range(3)]
    box = "".join(rng.sample("ROYGBV", len(FACES)))
    turns = rotations()
    pieces = []
    for i, a in enumerate(cuts[0]):
        for j, b in enumerate(cuts[1]):
            for k, c in enumerate(cuts[2]):
                place = (i, j, k)
                colors = ""
                for axis in range(3):
                    end = len(cuts[axis]) - 1
                    colors += box[2 * axis] if place[axis] == 0 else "."
                    colors += box[2 * axis + 1] if place[axis] == end else "."
                dims = (a, b, c)
                p = rng.choice(turns)
                turned = [dims[p[2 * x] // 2] for x in range(3)]
                pieces.append("%d %d %d %s" % (
                    turned[0], turned[1], turned[2], "".join(colors[p[f]] for f in range(6))))
    rng.shuffle(pieces)
    print(sum(cuts[0]), sum(cuts[1]), sum(cuts[2]), box)
    print(len(pieces))
    print("\n".join(pieces))


main()
