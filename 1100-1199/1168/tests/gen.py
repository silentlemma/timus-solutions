"""A map with radio stations: a seed, M, N, K, the highest altitude, the
largest radius and a mode. Mode 0 gives random radii, mode 1 radii close to
whole numbers between half the largest and the largest (so rounding
matters), mode 2 radii of 0 and whole numbers, mode 3 random radii between
half the largest and the largest."""

import random
import sys

NEAR = 0.001


def main():
    seed, m, n, k, top, reach, mode = (int(x) for x in sys.argv[1:8])
    rng = random.Random(seed)
    lines = ["%d %d %d" % (m, n, k)]
    for _ in range(m):
        lines.append(" ".join(str(rng.randint(0, top)) for _ in range(n)))
    cells = rng.sample([(i, j) for i in range(1, m + 1) for j in range(1, n + 1)], k)
    for i, j in cells:
        if mode == 1:
            r = "%.3f" % (rng.randint(reach // 2, reach) + rng.choice([-NEAR, 0, NEAR]))
        elif mode == 2:
            r = str(rng.choice([0, rng.randint(0, reach)]))
        elif mode == 3:
            r = "%.2f" % rng.uniform(reach / 2, reach)
        else:
            r = "%.2f" % rng.uniform(0, reach)
        lines.append("%d %d %s" % (i, j, r))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
