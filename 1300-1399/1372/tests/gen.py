"""Deterministic stations: gen.py SEED MODE [N], N defaults to 9 (1..9).

Modes:
  poles: random places and directions within 0.01 degree of either pole;
         maximum radius, mass, mast height 100 and thrust.
  radial: random places with almost radial inward or outward pushes;
          angular perturbations of 0.00001 through 0.001 degree.
  pairs: random swapped place/direction pairs with opposite torques,
         shuffled with an unpaired engine when N is odd.
"""

import random
import sys


def main():
    seed, mode = int(sys.argv[1]), sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 9
    if not 1 <= n <= 9:
        raise ValueError('N must be between 1 and 9')
    rng = random.Random(seed)

    def point():
        return rng.randrange(36000000) / 100000, rng.randrange(-9000000, 9000001) / 100000

    engines = []
    if mode == 'poles':
        print('2000 40000000 100')
        print(100000, n)
        for _ in range(n):
            row = []
            for _ in range(2):
                row.extend((rng.randrange(36000000) / 100000,
                            rng.choice((-1, 1)) * (90 - rng.randint(0, 1000) / 100000)))
            engines.append(row)
    elif mode == 'radial':
        print('100 40000000 0')
        print(100000, n)
        for _ in range(n):
            lon, lat = point()
            dlon, dlat = (lon, lat) if rng.randrange(2) else ((lon + 180) % 360, -lat)
            dlon = (dlon + rng.choice((-1, 1)) * rng.randint(1, 100) / 100000) % 360
            engines.append((lon, lat, dlon, dlat))
    elif mode == 'pairs':
        print('1234.5 12345678.9 67.89')
        print(99999, n)
        for _ in range(n // 2):
            a, b = point(), point()
            engines.extend(((*a, *b), (*b, *a)))
        if n % 2:
            engines.append((*point(), *point()))
        rng.shuffle(engines)
    else:
        raise ValueError('unknown mode')
    for row in engines:
        print(' '.join(f'{v:.5f}' for v in row))


if __name__ == '__main__':
    main()
