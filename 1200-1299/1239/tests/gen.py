"""Ghosts: a seed, N and a mode. Mode 1 scatters them anywhere; mode 2
crowds large ones around one direction, so many overlap; mode 3 builds
them from a few ghosts by scaling and swapping coordinates, so many cones
coincide or mirror each other."""

import random
import sys

TOP = 10000
BASES = 4


def ghost(rng, x, y, z, small=False):
    top = min(x, y, z)
    return (x, y, z, rng.randint(1, max(1, top // 10)) if small else rng.randint(1, top))


def main():
    seed, n, mode = (int(v) for v in sys.argv[1:4])
    rng = random.Random(seed)
    ghosts = []
    if mode == 1:
        for _ in range(n):
            ghosts.append(ghost(rng, *(rng.randint(1, TOP) for _ in range(3)), small=True))
    elif mode == 2:
        axis = [rng.randint(1, 10) for _ in range(3)]
        for _ in range(n):
            k = rng.randint(50, TOP // 10)
            x, y, z = (max(1, min(TOP, a * k + rng.randint(-k // 2, k // 2))) for a in axis)
            ghosts.append(ghost(rng, x, y, z))
    else:
        bases = [ghost(rng, *(rng.randint(1, TOP // 10) for _ in range(3))) for _ in range(BASES)]
        for _ in range(n):
            x, y, z, r = rng.choice(bases)
            k = rng.randint(1, 10)
            coords = [x * k, y * k, z * k]
            rng.shuffle(coords)
            ghosts.append((*coords, r * k))
    lines = [str(len(ghosts))] + ["%d %d %d %d" % g for g in ghosts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
