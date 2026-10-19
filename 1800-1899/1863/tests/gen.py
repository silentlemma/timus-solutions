"""A log of moves from a seed and a mode: mode 1 a few moves, 2 the most
moves on the deepest reactor, 3 the most moves on a shallow reactor, so
that many depths repeat, 4 the most moves of powers of two, 5 the most
moves, each nearly as long as the depth allows, 6 the most moves of
small steps, 7 a million distinct first-half depths followed by a full-depth
move and seeded random small steps. The moves follow a hidden path that stays
within the reactor."""

import random
import sys

MOST = 40
DEPTH = 10 ** 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 7:
        moves = [1 << i for i in range(MOST // 2)]
        s = sum(moves)
        rng.shuffle(moves)
        # Subtracting every first-half move reaches zero; the full-depth
        # move then leaves just that path, after all 2**20 depths were built.
        moves.append(DEPTH)
        depth = DEPTH
        while len(moves) < MOST:
            d = rng.randint(1, 1000)
            ways = [x for x in (depth + d, depth - d) if 0 <= x <= DEPTH]
            depth = rng.choice(ways)
            moves.append(d)
        print(DEPTH, s, MOST)
        print(*moves)
        return
    k = rng.randint(1, 12) if mode == 1 else MOST
    n = {1: rng.randint(1, 30), 3: rng.randint(10, 100)}.get(mode, DEPTH)
    s = rng.randint(0, n)
    depth, moves = s, []
    while len(moves) < k:
        if mode == 4:
            d = 1 << rng.randint(0, n.bit_length() - 2)
        elif mode == 5:
            far = max(depth, n - depth)
            d = rng.randint(max(1, far - n // 50), far)
        elif mode == 6:
            d = rng.randint(1, 1000)
        else:
            d = rng.randint(1, n)
        ways = [x for x in (depth + d, depth - d) if 0 <= x <= n]
        if ways:
            depth = rng.choice(ways)
            moves.append(d)
    print(n, s, k)
    print(*moves)


main()
