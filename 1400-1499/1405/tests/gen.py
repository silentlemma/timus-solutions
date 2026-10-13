"""Gardens of 1000 trees: a seed and a mode. Mode 1 is random, mode 2
crowds most trees into a small square so that few can take a goat, mode 3
is a grid with 3 meters between neighbours, mode 4 places pairs of trees
exactly 1 meter apart, so every rope is exactly 1 meter."""

import random
import sys

N = 1000
TOP = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    trees = set()
    if mode == 1:
        while len(trees) < N:
            trees.add((rng.randint(-TOP * 100, TOP * 100), rng.randint(-TOP * 100, TOP * 100)))
    elif mode == 2:
        trees |= {(-9000, -9000), (9000, 9000), (-9000, 9000)}
        while len(trees) < N:
            trees.add((rng.randint(-300, 300), rng.randint(-300, 300)))
    elif mode == 3:
        for i in range(-15, 16):
            for j in range(-15, 16):
                if len(trees) < N:
                    trees.add((300 * i, 300 * j))
    else:
        for k in range(N // 2):
            x, y = -9000 + (k % 25) * 700, -9000 + (k // 25) * 450
            trees |= {(x, y), (x + 100, y)}
    trees = list(trees)
    rng.shuffle(trees)
    print(len(trees))
    for x, y in trees:
        print("%.2f %.2f" % (x / 100, y / 100))


main()
