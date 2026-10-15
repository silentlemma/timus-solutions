"""One test from a seed and a mode: random attack directions for one of
the five solids (mode 1 a few attacks, mode 2 a hundred, mode 3 a hundred
attacks from three directions, so that guns often already point there)."""

import random
import sys

SOLIDS = ["tetrahedron", "hexahedron", "octahedron", "dodecahedron", "icosahedron"]
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    name = SOLIDS[seed % len(SOLIDS)]
    n = rng.randint(1, 5) if mode == 1 else MOST
    print(name)
    print(n)
    def direction():
        while True:
            v = [rng.uniform(-1, 1) for _ in range(3)]
            if sum(c * c for c in v) > 0.01:
                return v

    few = [direction() for _ in range(3)]
    for _ in range(n):
        v = rng.choice(few) if mode == 3 else direction()
        print(" ".join("%.5f" % c for c in v))


main()
