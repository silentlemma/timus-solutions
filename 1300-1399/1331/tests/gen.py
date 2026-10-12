"""A seed and a mode; modes 1-4 give 5000 artifacts and 5000 pads.
Mode 1 gives random
points over the whole planet, mode 2 pads crowded near the north pole
and artifacts near the south pole, mode 3 points close to the date line
on both sides, mode 4 a planet of radius 1000 and pads at the very
places of some artifacts. Mode 5 gives 5000 artifacts and one pad;
mode 6 gives one artifact and 5000 pads with the nearest pad last;
mode 7 gives 5000 equatorial pads and 5000 artifacts, including points
very close to both poles."""

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
    if mode in (5, 6, 7):
        if mode == 5:
            pads = [(23.456789, -135.246810)]
            found = [point(rng, 1) for _ in range(N)]
        elif mode == 6:
            found = [(45.678901, 87.654321)]
            pads = [(rng.uniform(-LAT, -30), rng.uniform(-LON, LON)) for _ in range(N - 1)]
            pads.append((45.679801, 87.654321))
        else:
            pads = [(0, -LON + 2 * LON * i / N) for i in range(N)]
            found = [
                (
                    rng.choice([-89.999999, 89.999999]) if i % 3 == 0 else rng.uniform(-LAT, LAT),
                    rng.uniform(-LON, LON),
                )
                for i in range(N)
            ]
        print(len(found), len(pads))
        print("1000.000000")
        for lat, lon in pads + found:
            print("%.6f %.6f" % (lat, lon))
        return
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
