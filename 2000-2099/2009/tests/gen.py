"""Usage: gen.py SEED MODE.

Modes: none,anchor,individual,departed_friend,gaps,late,dense,future,crowd,staggered.
All modes have 1000 students; dense modes have 100 directed friends per student.
"""

import random
import sys

COUNT = 1000
MAX_FRIENDS = 100
LAST_TIME = 1000000000
GAP = 999000
CROWD = 900
GROUP_SIZE = 10


def generate(seed, mode):
    rng = random.Random(seed)
    friends = [[] for _ in range(COUNT)]
    if mode == "anchor":
        friends = [[]] + [[0] for _ in range(COUNT - 1)]
    elif mode == "departed_friend":
        friends = [[]] + [[i - 1] for i in range(1, COUNT)]
    elif mode == "future":
        friends = [[(i + j) % COUNT for j in range(1, MAX_FRIENDS + 1)] for i in range(COUNT)]
    elif mode in ("dense", "crowd", "staggered"):
        for i in range(COUNT):
            pool = list(range(COUNT))
            pool.pop(i)
            friends[i] = rng.sample(pool, MAX_FRIENDS)
    elif mode not in ("none", "individual", "gaps", "late"):
        raise ValueError("unknown mode")
    if mode in ("individual", "departed_friend"):
        groups = [(i + 1, [i]) for i in range(COUNT)]
    elif mode == "gaps":
        groups = [(1 + i * GAP, [i]) for i in range(COUNT)]
    elif mode == "late":
        groups = [(LAST_TIME, list(range(COUNT)))]
    elif mode == "crowd":
        groups = [(1, list(range(CROWD))), (2, list(range(CROWD, COUNT)))]
    elif mode == "staggered":
        groups = [
            (i // GROUP_SIZE + 1, list(range(i, i + GROUP_SIZE)))
            for i in range(0, COUNT, GROUP_SIZE)
        ]
    else:
        groups = [(1, list(range(COUNT)))]
    return friends, groups


if __name__ == "__main__":
    friends, groups = generate(int(sys.argv[1]), sys.argv[2])
    print(len(friends), len(groups))
    for row in friends:
        print(*(person + 1 for person in row), 0)
    for time, students in groups:
        print(time, len(students))
        print(*(person + 1 for person in students))
