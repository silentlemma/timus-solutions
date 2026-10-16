"""One test from a seed and a mode: mode 1 a random sequence on few
pedestals, mode 2 a two-way sweep with random touches before and after
it, mode 3 the same with one touch of the sweep moved by one, mode 4 a
random sequence on many pedestals, mode 5 the largest two-way sweep,
mode 6 random touches with both n and m maximal, mode 7 two pedestals
evading until the final touch, mode 8 alternating walls at maximal odd n."""

import random
import sys

LIMIT = 100000
FEW = 8


def sweep(rng, n):
    forward = list(range(2, n))
    passes = [forward, forward[::-1]]
    if rng.random() < 0.5:
        passes = [forward[::-1], forward]
    return passes[0] + passes[1] if n > 2 else [1, 1]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, FEW)
        touches = [rng.randint(1, n) for _ in range(rng.randint(2, FEW * 2))]
    elif mode in (2, 3):
        n = rng.randint(2, LIMIT // 2)
        core = sweep(rng, n)
        if mode == 3:
            k = rng.randrange(len(core))
            core[k] = core[k] + 1 if core[k] < n else core[k] - 1
        room = LIMIT - len(core)
        before = [rng.randint(1, n) for _ in range(rng.randint(0, room // 2))]
        after = [rng.randint(1, n) for _ in range(rng.randint(0, room // 2))]
        touches = before + core + after
    elif mode == 4:
        n = rng.randint(2, LIMIT)
        touches = [rng.randint(1, n) for _ in range(LIMIT)]
    elif mode == 6:
        n = LIMIT
        touches = [rng.randint(1, n) for _ in range(LIMIT)]
    elif mode == 7:
        n = 2
        touches = [1, 2] * (LIMIT // 2)
        touches[-1] = touches[-2]
    elif mode == 8:
        n = LIMIT - 1
        touches = [1, n] * (LIMIT // 2)
    else:
        n = LIMIT // 2 + 2
        touches = sweep(rng, n)
    print(n, len(touches))
    print(*touches)


main()
