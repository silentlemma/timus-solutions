"""A battle: a seed and a mode. Mode 1 draws every number in its full
range; mode 2 takes the largest field, pack and mana with a hero whose
hit points are drawn low, so the verdict is often close; mode 3 lets the
monsters cover the whole field in one move."""

import random
import sys

TOP_N, TOP_HP, TOP_MANA, TOP_HPM, TOP_COUNT, TOP_BOLT = 10, 100, 50, 10, 10, 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = TOP_N if mode == 2 else rng.randint(1, TOP_N)
    hp = rng.randint(2, TOP_HP // 4) if mode == 2 else rng.randint(2, TOP_HP)
    mana = TOP_MANA if mode == 2 else rng.randint(1, TOP_MANA)
    hpm = TOP_HPM if mode == 2 else rng.randint(1, TOP_HPM)
    count = TOP_COUNT if mode == 2 else rng.randint(1, TOP_COUNT)
    speed = n if mode == 3 else rng.randint(1, n)
    heal = rng.randint(1, hp - 1)
    bolts = [rng.randint(1, TOP_BOLT) for _ in range(n)]
    sys.stdout.write(
        "%d %d %d %d %d %d %d\n%s\n"
        % (n, hp, mana, hpm, count, speed, heal, " ".join(map(str, bolts)))
    )


if __name__ == "__main__":
    main()
