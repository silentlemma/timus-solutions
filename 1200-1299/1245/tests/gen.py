"""Blood spots: a seed, N and a mode. Mode 1 scatters spots of any size;
mode 2 puts small spots in two clusters; mode 3 puts small spots in two
clusters whose spans overlap on one axis; mode 4 lines spots up along one
axis."""

import random
import sys

TOP = 10000
SMALL = 50
CLUSTER = 1000


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    spots = []
    centres = [
        (rng.randint(CLUSTER, TOP - CLUSTER), rng.randint(CLUSTER, TOP - CLUSTER)) for _ in range(2)
    ]
    if mode == 3:
        centres[1] = (TOP - centres[0][0], centres[0][1] + rng.randint(-CLUSTER, CLUSTER) // 2)
    for _ in range(n):
        if mode == 1:
            spots.append((rng.randint(1, TOP), rng.randint(1, TOP), rng.randint(1, TOP)))
        elif mode == 4:
            spots.append((rng.randint(1, SMALL), rng.randint(SMALL, TOP - SMALL), TOP // 2))
        else:
            cx, cy = rng.choice(centres)
            spots.append(
                (
                    rng.randint(1, SMALL),
                    cx + rng.randint(-CLUSTER // 2, CLUSTER // 2),
                    cy + rng.randint(-CLUSTER // 2, CLUSTER // 2),
                )
            )
    lines = [str(n)] + ["%d %d %d" % s for s in spots]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
