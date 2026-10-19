"""Usage: seed mode. Modes: random, all_ties, no_friends, impossible,
alone_wins, share_wins, odd_boundary, last_friend, one_room.
All have 256 apartments; all except no_friends have 256 possible roommates.
"""

import random
import sys

COUNT = 256
MAX_VALUE = 100000
HALF = MAX_VALUE // 2


def generate(seed, mode):
    rng = random.Random(seed)
    budget = MAX_VALUE
    alone = [0, 0]
    friends = [(MAX_VALUE, 0)] * COUNT
    apartments = [(2, MAX_VALUE, 0)] * COUNT
    if mode in ("random", "no_friends", "one_room"):
        budget = rng.randint(1, MAX_VALUE)
        alone = [rng.randint(0, MAX_VALUE) for _ in range(2)]
        friends = [(rng.randint(1, MAX_VALUE), rng.randint(0, MAX_VALUE)) for _ in range(COUNT)]
        apartments = [
            (
                1 if mode == "one_room" else rng.randint(1, 2),
                rng.randint(1, MAX_VALUE),
                rng.randint(0, MAX_VALUE),
            )
            for _ in range(COUNT)
        ]
        if mode == "no_friends":
            friends = []
    elif mode == "impossible":
        budget = 1
        friends = [(1, MAX_VALUE)] * COUNT
        apartments = [(2, MAX_VALUE, MAX_VALUE)] * COUNT
    elif mode == "alone_wins":
        alone = [MAX_VALUE, MAX_VALUE]
        apartments[-1] = (2, MAX_VALUE, MAX_VALUE)
    elif mode in ("share_wins", "last_friend"):
        budget = HALF
        friends = [(HALF if mode == "share_wins" else 1, 0)] * COUNT
        friends[-1] = (HALF, MAX_VALUE)
        apartments[-1] = (2, MAX_VALUE, MAX_VALUE)
    elif mode == "odd_boundary":
        budget = HALF - 1
        friends = [(HALF, 0)] * COUNT
        friends[-1] = (HALF - 2, MAX_VALUE)
        apartments = [(2, MAX_VALUE - 1, MAX_VALUE)] * COUNT
        apartments[-1] = (2, MAX_VALUE - 2, MAX_VALUE)
    elif mode != "all_ties":
        raise ValueError("unknown mode")
    lines = [f"{budget} {alone[0]} {alone[1]}", str(len(friends))]
    lines.extend(f"{money} {value}" for money, value in friends)
    lines.append(str(len(apartments)))
    lines.extend(f"{rooms} {price} {value}" for rooms, price, value in apartments)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
