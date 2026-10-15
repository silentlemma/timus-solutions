"""One test from a seed and a mode: mode 1 a random separable permutation
of up to 10 elements, mode 2 a random separable permutation of 10000,
mode 3 a random permutation (almost never separable), mode 4 a separable
permutation of 10000 alternating direct and skew joins as deeply as
possible, mode 5 a separable one with one pair swapped, mode 6 the reverse
permutation of 10000, mode 7 an increasing prefix followed by a forbidden
pattern at the upper boundary, mode 8 a balanced alternating join tree of
10000, mode 9 all even values followed by all odd values at size 10000."""

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
    elif mode == 6:
        perm = list(range(MOST, 0, -1))
    elif mode == 7:
        perm = list(range(1, MOST - 3))
        perm += [MOST - 2, MOST, MOST - 3, MOST - 1]
    elif mode == 8:
        perm = []
        todo = [(1, MOST, rng.randrange(2))]
        while todo:
            lo, hi, up = todo.pop()
            if lo == hi:
                perm.append(lo)
                continue
            mid = (lo + hi) // 2
            low, high = (lo, mid, not up), (mid + 1, hi, not up)
            first, second = (low, high) if up else (high, low)
            todo.extend([second, first])
    elif mode == 9:
        perm = list(range(2, MOST + 1, 2)) + list(range(1, MOST + 1, 2))
    else:
        perm = separable(rng, 1, rng.randint(4, 12), False)
        i, j = rng.sample(range(len(perm)), 2)
        perm[i], perm[j] = perm[j], perm[i]
    print(len(perm))
    print(*perm)


main()
