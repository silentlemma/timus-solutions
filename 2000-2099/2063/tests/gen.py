"""99 games with rows of 2..100 balls from a seed and a mode: 1 random
colours, 2 rows with both colours and a random boundary, 3 black first then
white, 4 alternating colours, 5 one ball of the other colour, 6 a single
colour."""

import random
import sys

GAMES = 99


def row(rng, n, mode):
    if mode == 1:
        return "".join(rng.choice("01") for _ in range(n))
    if mode == 2:
        while True:
            r = "".join(rng.choice("01") for _ in range(n))
            if "0" in r and "1" in r:
                return r
    if mode == 3:
        k = rng.randint(1, n - 1)
        return "1" * k + "0" * (n - k)
    if mode == 4:
        return "".join("10"[i % 2] for i in range(n))
    if mode == 5:
        r = [rng.choice("01")] * n
        i = rng.randrange(n)
        r[i] = "1" if r[i] == "0" else "0"
        return "".join(r)
    return rng.choice("01") * n


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(GAMES)
    for game in range(GAMES):
        print(row(rng, game + 2, mode))


main()
