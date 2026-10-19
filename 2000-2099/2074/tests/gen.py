"""A random classifier from a seed: up to 20 topics in a tree, up to 20
problem numbers, each topic listing a random subset of them over one or
more lines. Full topic descriptions are kept distinct."""

import random
import sys

MAX_TOPICS = 20
MAX_PROBLEMS = 20
LOW, HIGH = 1000, 9999
WORDS = ["dp", "graphs", "geometry", "idea", "technique", "trees", "games", "a", "b"]
MAX_NAME_WORDS = 2
SHARE = 0.3  # chance that a topic lists a problem


def main():
    rng = random.Random(int(sys.argv[1]))
    problems = rng.sample(range(LOW, HIGH + 1), rng.randint(1, MAX_PROBLEMS))
    ids = []  # id of each listed topic as a list of numbers
    for _ in range(rng.randint(1, MAX_TOPICS)):
        if not ids:
            ids.append([1])
            continue
        last = ids[-1]
        # go one level deeper, or take the next sibling of some ancestor
        choice = rng.randrange(len(last) + 1)
        ids.append(last + [1] if choice == len(last) else last[:choice] + [last[choice] + 1])
    full = {}  # id -> full description
    for topic in ids:
        parent = full.get(tuple(topic[:-1]))
        while True:
            name = " ".join(rng.choice(WORDS) for _ in range(rng.randint(1, MAX_NAME_WORDS)))
            description = name if parent is None else parent + "." + name
            if description not in full.values():
                break
        full[tuple(topic)] = description
        print("".join("%d." % x for x in topic), name)
        own = [p for p in problems if rng.random() < SHARE]
        rng.shuffle(own)
        while own:
            k = rng.randint(1, len(own))
            print(" ".join(map(str, own[:k])))
            own = own[k:]


main()
