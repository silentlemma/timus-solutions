"""A position: a seed, N and the mode. valid: the position after a random
number of steps of the optimal algorithm; random: any rods for the disks
(almost always unreachable); last: the position after the last step."""

import random
import sys


def position(n, step):
    """The rods of disks 1..n after the given step of moving them 1 -> 2."""
    rods = [0] * (n + 1)
    a, b, c = 1, 2, 3
    for disk in range(n, 0, -1):
        half = 1 << (disk - 1)
        if step < half:
            rods[disk] = a
            b, c = c, b
        else:
            rods[disk] = b
            step -= half
            a, c = c, a
    return rods[1:]


def main():
    seed, n, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    if mode == "valid":
        rods = position(n, rng.randrange(1 << n))
    elif mode == "last":
        rods = position(n, (1 << n) - 1)
    else:
        rods = [rng.randint(1, 3) for _ in range(n)]
    sys.stdout.write("\n".join(map(str, [n] + rods)) + "\n")


if __name__ == "__main__":
    main()
