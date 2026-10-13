"""A grey picture: a seed and a mode. Mode 1 gives 300 x 300 random
noise, mode 2 a 75 x 97 picture of the single grey 46, where rounding
every row from the left breaks the limit at the right border, mode 3 a
smooth 300 x 300 gradient, mode 4 random grey rectangles, mode 5 the
smallest size with one grey per row, mode 6 a tall picture of middle
grey."""

import random
import sys

TOP = 255
SMALL = 75
LARGE = 300


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = m = LARGE
        pic = [[rng.randint(0, TOP) for _ in range(m)] for _ in range(n)]
    elif mode == 2:
        n, m = SMALL, 97
        pic = [[46] * m for _ in range(n)]
    elif mode == 3:
        n = m = LARGE
        pic = [[(i + j) * TOP // (n + m - 2) for j in range(m)] for i in range(n)]
    elif mode == 4:
        n, m = 200, 250
        pic = [[rng.randint(0, TOP)] * m for _ in range(n)]
        for _ in range(60):
            top, left = rng.randrange(n), rng.randrange(m)
            h, w, grey = rng.randint(1, 80), rng.randint(1, 80), rng.randint(0, TOP)
            for i in range(top, min(n, top + h)):
                pic[i][left : min(m, left + w)] = [grey] * (min(m, left + w) - left)
    elif mode == 5:
        n = m = SMALL
        pic = [[rng.randint(0, TOP)] * m for _ in range(n)]
    else:
        n, m = LARGE, SMALL
        pic = [[TOP // 2 + 1] * m for _ in range(n)]
    print(n, m)
    for row in pic:
        print(" ".join(map(str, row)))


main()
