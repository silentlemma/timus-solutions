"""Maze maps and commands: a seed and a mode. Mode 1 is a torus of shifts,
where every command is a permutation, mode 2 a maze with walls, mode 3
random permutations, mode 4 permutations that each merge one pair of
cells, mode 5 random maps; all on a 100 x 100 field with 4000 commands."""

import random
import sys

SIDE = 100
COMMANDS = 4000
MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))
WALL_SHARE = 0.3


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = m = SIDE
    cells = [(r, c) for r in range(n) for c in range(m)]
    maps = []
    if mode == 1:
        for dr, dc in MOVES:
            maps.append([((r + dr) % n, (c + dc) % m) for r, c in cells])
    elif mode == 2:
        # a wall between two neighbours blocks the move both ways
        walls = set()
        for r, c in cells:
            for dr, dc in MOVES[1::2]:
                if rng.random() < WALL_SHARE:
                    walls.add(((r, c), (r + dr, c + dc)))
        for dr, dc in MOVES:
            image = []
            for r, c in cells:
                t = (r + dr, c + dc)
                blocked = ((r, c), t) in walls or (t, (r, c)) in walls
                inside = 0 <= t[0] < n and 0 <= t[1] < m
                image.append(t if inside and not blocked else (r, c))
            maps.append(image)
    else:
        for _ in MOVES:
            image = cells[:]
            rng.shuffle(image)
            if mode == 4:
                a, b = rng.sample(range(len(cells)), 2)
                image[a] = image[b]
            elif mode == 5:
                image = [rng.choice(cells) for _ in cells]
            maps.append(image)
    out = ["%d %d" % (n, m)]
    for image in maps:
        for r in range(n):
            out.append(
                "  ".join("%d %d" % (tr + 1, tc + 1) for tr, tc in image[r * m : (r + 1) * m])
            )
    out.append(str(COMMANDS))
    out.append(" ".join(str(rng.randint(1, 4)) for _ in range(COMMANDS)))
    print("\n".join(out))


main()
