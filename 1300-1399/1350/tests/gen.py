"""A canteen: a seed and a mode.

Mode 1: 100 products, 100 students and random dangers.
Mode 2: a first student who fears almost everything.
Mode 3: nothing in the meal at all.
Mode 4: 40-character names and maximum nonempty-meal input size.
Mode 5: a small random menu whose possible meals can all be enumerated.
"""

import random
import string
import sys

N = 100
K = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (4, 5):
        special(rng, mode)
        return
    names = set()
    while len(names) < N:
        names.add("".join(rng.choices(string.ascii_letters + string.digits, k=rng.randint(1, 40))))
    menu = sorted(names)
    rng.shuffle(menu)
    first = rng.sample(menu, N - rng.randint(1, 5) if mode == 2 else rng.randint(0, N // 2))
    safe = [p for p in menu if p not in first]
    m = 0 if mode == 3 else rng.randint(0, len(safe))
    print(N)
    print("\n".join(menu))
    print(K)
    for danger in [first] + [rng.sample(menu, rng.randint(0, N)) for _ in range(K)]:
        print(len(danger))
        for p in danger:
            print(p)
    print(m)


def special(rng, mode):
    if mode == 4:
        menu = ["P" * 38 + f"{i:02d}" for i in range(N)]
        rng.shuffle(menu)
        first = rng.sample(menu, N - 1)
        students = [rng.sample(menu, N) for _ in range(K)]
        m = 1
    else:
        menu = rng.sample(list(string.ascii_letters + string.digits), 8)
        first = rng.sample(menu, 2)
        students = [rng.sample(menu, rng.randint(0, len(menu))) for _ in range(K)]
        m = 3
    print(len(menu))
    print("\n".join(menu))
    print(len(students))
    for danger in [first] + students:
        print(len(danger))
        for product in danger:
            print(product)
    print(m)


main()
