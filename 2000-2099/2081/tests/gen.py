"""Timer readings from a seed: a random strictly decreasing sequence of times,
each lit segment dropped with some chance.

Mode 1: a few readings, half the segments lost. Mode 2: 100 readings, a few
segments lost. Mode 3: 100 readings close together, most segments lost.
Mode 4: 100 readings with every segment lost.
"""

import random
import sys

DIGITS = [
    "._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
    "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|",
]
COLUMNS = [0, 4, 10, 14]
WIDTH = 3
LINE = 17
COLON = 8  # the column with the asterisks
SECONDS = 60
MAX_N = 100
FEW = 5
LOSS = {1: 0.5, 2: 0.1, 3: 0.8, 4: 1.0}


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 1 else MAX_N
    top = MAX_N * 2 if mode == 3 else SECONDS * SECONDS
    times = sorted(rng.sample(range(top), n), reverse=True)
    print(n)
    for value in times:
        m, s = divmod(value, SECONDS)
        rows = [["."] * LINE for _ in range(WIDTH)]
        rows[1][COLON] = rows[2][COLON] = "*"
        for c, d in zip(COLUMNS, (m // 10, m % 10, s // 10, s % 10)):
            for i, ch in enumerate(DIGITS[d]):
                if ch != "." and rng.random() >= LOSS[mode]:
                    rows[i // WIDTH][c + i % WIDTH] = ch
        for row in rows:
            print("".join(row))


main()
