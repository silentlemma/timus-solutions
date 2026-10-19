"""A delegation from a seed and a mode: mode 1 a few blocks, 2 the most
blocks with small groups of friends, 3 the most blocks with large
groups, 4 the most blocks with no friends at all, 5 the most blocks
where every block is one group, 6 the most blocks with groups that fit
together in few ways, 7 the most blocks, each of two groups with one
side seat and some compartment seats plus groups of compartment seats.
The people of every block of a hidden seating are split into groups,
every group is joined by friendships, and everybody gets a random
number.
Modes 8-10 also use the maximum 1000 blocks: 8 complete friendship graphs
in every block (15000 edges), 9 four-person compartment groups and 2000
single side passengers, 10 equal numbers of four/two and three/three
filler gadgets requiring different pairings of one-side groups.
"""

import random
import sys

MOST = 1000
SMALL = 4


def structured(seed, mode):
    rng = random.Random(seed)
    if mode == 8:
        groups = [(4, 2)] * MOST
    elif mode == 9:
        groups = [(4, 0), (0, 1), (0, 1)] * MOST
    elif mode == 10:
        groups = []
        for i in range(MOST // 2):
            groups.extend([(1, 1), (1, 1), (0, 1), (0, 1)])
            groups.extend([(4, 0), (2, 0)] if i % 2 == 0 else [(3, 0), (3, 0)])
    else:
        raise ValueError("unknown mode")
    label = list(range(1, 6 * MOST + 1))
    rng.shuffle(label)
    wish, pairs, start = [""] * (6 * MOST), [], 0
    for a, b in groups:
        people = label[start:start + a + b]
        start += a + b
        for p, c in zip(people, "1" * a + "0" * b):
            wish[p - 1] = c
        if mode == 8:
            pairs.extend((min(p, q), max(p, q))
                         for i, p in enumerate(people) for q in people[i + 1:])
        else:
            pairs.extend((min(p, people[i - 1]), max(p, people[i - 1]))
                         for i, p in enumerate(people) if i)
    rng.shuffle(pairs)
    print(MOST)
    print("".join(wish))
    print(len(pairs))
    print("\n".join("%d %d" % p for p in pairs))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    if mode >= 8:
        structured(seed, mode)
        return
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else MOST
    label = list(range(1, 6 * n + 1))
    rng.shuffle(label)
    wish = [""] * (6 * n)
    pairs = set()
    shapes = [[4, 2], [3, 1, 1, 1], [2, 2, 2], [1, 1, 1, 1, 1, 1], [5, 1], [3, 3]]
    for block in range(n):
        people = label[6 * block:6 * block + 6]
        seats = list("111100")
        rng.shuffle(seats)
        for p, c in zip(people, seats):
            wish[p - 1] = c
        if mode == 4:
            continue
        if mode == 7:
            ones = [p for p in people if wish[p - 1] == "1"]
            sides = [p for p in people if wish[p - 1] == "0"]
            first = rng.randint(0, 4)
            second = rng.randint(0, 4 - first)
            people = [sides[0]] + ones[:first] + [sides[1]] + ones[first:]
            sizes = [1 + first, 1 + second]
            left = 4 - first - second
            while left:
                size = rng.randint(1, left)
                sizes.append(size)
                left -= size
        elif mode == 5:
            sizes = [6]
        elif mode == 6:
            sizes = rng.choice(shapes)
        else:
            sizes, left = [], 6
            while left:
                most = 2 if mode == 2 else left
                size = rng.randint(1, min(most, left))
                sizes.append(size)
                left -= size
        start = 0
        for size in sizes:
            group = people[start:start + size]
            start += size
            for i in range(1, size):
                a, b = group[i], group[rng.randrange(i)]
                pairs.add((min(a, b), max(a, b)))
            for _ in range(rng.randint(0, size)):
                a, b = rng.sample(group, 2) if size > 1 else (0, 0)
                if a:
                    pairs.add((min(a, b), max(a, b)))
    pairs = sorted(pairs)
    rng.shuffle(pairs)
    print(n)
    print("".join(wish))
    print(len(pairs))
    print("\n".join("%d %d" % p for p in pairs))


main()
