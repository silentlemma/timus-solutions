"""N first-years with random names: a seed, N and the longest name.
Names mix letters of both cases, spaces and hyphens; every house gets
at least one student."""

import random
import string
import sys

HOUSES = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"]


def main():
    seed, n, longest = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    houses = HOUSES + [rng.choice(HOUSES) for _ in range(n - len(HOUSES))]
    rng.shuffle(houses)
    lines = [str(n)]
    for house in houses:
        size = rng.randint(1, longest)
        name = [rng.choice(string.ascii_letters + " -") for _ in range(size)]
        name[0] = name[-1] = rng.choice(string.ascii_letters)
        lines += ["".join(name), house]
    print("\n".join(lines))


main()
