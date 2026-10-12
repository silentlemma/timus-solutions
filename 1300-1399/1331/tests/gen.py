"""5000 artifacts and 5000 pads: a seed and a mode. Mode 1 gives random
points over the whole planet, mode 2 pads crowded near the north pole
and artifacts near the south pole, mode 3 points close to the date line
on both sides, mode 4 a planet of radius 1000 and pads at the very
places of some artifacts."""

import random
import sys

N = 5000
LAT = 90
LON = 180


def point(rng, mode):
    if mode == 3:
        return rng.uniform(-LAT, LAT), rng.choice([-1, 1]) * rng.uniform(LON - 1, LON)
    return rng.uniform(-LAT, LAT), rng.uniform(-LON, LON)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    radius = 1000 if mode == 4 else rng.uniform(1, 1000)
    if mode == 2:
        pads = [(rng.uniform(LAT - 1, LAT), rng.uniform(-LON, LON)) for _ in range(N)]
        found = [(rng.uniform(-LAT, 1 - LAT), rng.uniform(-LON, LON)) for _ in range(N)]
    else:
        pads = [point(rng, mode) for _ in range(N)]
        found = [point(rng, mode) for _ in range(N)]
    if mode == 4:
        for i in range(0, N, 7):
            pads[i] = found[i * 3 % N]
    print(N, N)
    print("%.6f" % radius)
    for lat, lon in pads + found:
        print("%.6f %.6f" % (lat, lon))


main()
