"""A canteen: a seed and a mode. Mode 1 gives 100 products, 100 students
and random dangers, mode 2 a first student who fears almost everything,
mode 3 nothing in the meal at all."""

import random
import string
import sys

N = 100
K = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
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


main()
