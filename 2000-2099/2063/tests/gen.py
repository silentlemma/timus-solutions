"""99 games with rows of 2..100 balls from a seed and a mode: 1 random
colours, 2 rows with both colours and a random boundary, 3 black first then
white, 4 alternating colours, 5 one ball of the other colour, 6 a single
colour, 7 one white ball first and the rest black, 8 one black ball last and
the rest white, 9 black first then white with the boundary in the middle,
10 black first then white with the boundary next to an end, 11 a number of
black balls drawn uniformly from 0..n in random places, 12 mostly white,
13 mostly black."""

import random
import sys

GAMES = 99
FEW = 0.1  # the share of the rare colour in modes 12 and 13


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
    if mode == 7:
        return "0" + "1" * (n - 1)
    if mode == 8:
        return "0" * (n - 1) + "1"
    if mode == 9:
        return "1" * (n // 2) + "0" * (n - n // 2)
    if mode == 10:
        k = rng.choice([1, n - 1])
        return "1" * k + "0" * (n - k)
    if mode == 11:
        k = rng.randint(0, n)
        black = set(rng.sample(range(n), k))
        return "".join("1" if i in black else "0" for i in range(n))
    if mode in (12, 13):
        rare = "1" if mode == 12 else "0"
        common = "0" if mode == 12 else "1"
        return "".join(rare if rng.random() < FEW else common for _ in range(n))
    return rng.choice("01") * n


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(GAMES)
    for game in range(GAMES):
        print(row(rng, game + 2, mode))


main()
