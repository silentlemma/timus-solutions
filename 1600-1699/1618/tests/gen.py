"""One test from a seed and a mode: the deepToString of new Object[a1]...[an][0]
with a1 * ... * an <= 512 and at most 10^5 characters. Mode 1 random sizes,
mode 2 a long chain of ones with a few larger sizes, mode 3 one wide level,
mode 4 the largest product spread over several levels, mode 5 a level of
512 followed by as many levels of one as fit, mode 6 exactly 100 dimensions,
product 512 and 100000 printed characters."""

import random
import sys

MOST = 512
DEPTH = 100
LONGEST = 10**5


def show(dims):
    """deepToString of a uniform array, built bottom up"""
    text = "[]"
    for d in reversed(dims):
        text = "[" + ", ".join([text] * d) + "]"
    return text


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            dims, product = [], 1
            for _ in range(rng.randint(1, 12)):
                d = rng.randint(1, max(1, MOST // product))
                d = min(d, rng.randint(1, 6))
                dims.append(d)
                product *= d
        elif mode == 2:
            dims = [1] * rng.randint(20, DEPTH)
            for _ in range(rng.randint(1, 3)):
                dims[rng.randrange(len(dims))] = rng.randint(2, 4)
        elif mode == 3:
            dims = [rng.randint(100, MOST)]
        elif mode == 4:
            dims = rng.choice([[8, 8, 8], [2] * 9, [4, 2, 4, 4, 4], [16, 32], [512]])
        elif mode == 6:
            dims = [16, 4, 2, 1, 4] + [1] * 95
        else:
            dims = [MOST] + [1] * DEPTH
            while len(show(dims)) > LONGEST:
                dims.pop()
        product = 1
        for d in dims:
            product *= d
        text = show(dims)
        if product <= MOST and len(text) <= LONGEST:
            break
    print(text)


main()
