"""One test from a seed and a mode: mode 1 a random separable permutation
of up to 10 elements, mode 2 a random separable permutation of 10000,
mode 3 a random permutation (almost never separable), mode 4 a separable
permutation of 10000 alternating direct and skew joins as deeply as
possible, mode 5 a separable one with one pair swapped."""

import random
import sys

MOST = 10000


def separable(rng, lo, hi, deep):
    """A separable arrangement of lo..hi: split the values, arrange each
    part, put the parts in increasing or decreasing order."""
    out = []
    todo = [(lo, hi, rng.random() < 0.5)]
    while todo:
        a, b, up = todo.pop()
        if a == b:
            out.append(a)
            continue
        cut = a if deep else rng.randint(a, b - 1)
        low, high = (a, cut), (cut + 1, b)
        first, second = (low, high) if up else (high, low)
        # the second part goes on the stack first, so the first comes out first
        todo.append((second[0], second[1], not up if deep else rng.random() < 0.5))
        todo.append((first[0], first[1], not up if deep else rng.random() < 0.5))
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        perm = separable(rng, 1, rng.randint(1, 10), False)
    elif mode == 2:
        perm = separable(rng, 1, MOST, False)
    elif mode == 3:
        perm = list(range(1, rng.randint(4, MOST) + 1))
        rng.shuffle(perm)
    elif mode == 4:
        perm = separable(rng, 1, MOST, True)
    else:
        perm = separable(rng, 1, rng.randint(4, 12), False)
        i, j = rng.sample(range(len(perm)), 2)
        perm[i], perm[j] = perm[j], perm[i]
    print(len(perm))
    print(*perm)


main()
