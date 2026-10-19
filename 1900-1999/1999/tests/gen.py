"""Usage: gen.py SEED MODE; random1,random8,coprime1,coprime8,empty,all_nonempty,mod97,zero_only,unreachable,carry_chain."""

import random
import sys

BASE = 10
SIZE = 100


def generate(seed, mode):
    rng = random.Random(seed)
    n = SIZE
    old = [[rng.randrange(n) for _ in range(BASE)] for _ in range(n)]
    old[0][0] = 0
    flags = [0] + [rng.randrange(2) for _ in range(n - 1)]
    k = 1 if mode.endswith("1") else BASE - 2
    if mode.startswith("coprime") or mode == "carry_chain":
        for q in range(n):
            old[q][0] = 0 if q == 0 else 1 + q % (n - 1)
            old[q][BASE - 1] = (q + 1) % n
    if mode == "empty":
        flags = [0] * n
    elif mode == "all_nonempty":
        old[0] = [1] * BASE
        old[1] = [1] * BASE
        flags = [0] + [1] * (n - 1)
    elif mode == "mod97":
        modulus = 97
        n = modulus + 1
        old = [[0] * BASE for _ in range(n)]
        for d in range(1, BASE):
            old[0][d] = 1 + d % modulus
        for remainder in range(modulus):
            old[1 + remainder] = [1 + (BASE * remainder + d) % modulus for d in range(BASE)]
        flags = [0] * n
        flags[1] = 1
    elif mode == "zero_only":
        old[0] = [2] * BASE
        old[0][0] = 1
        old[1] = [2] * BASE
        old[1][0] = 1
        old[2] = [2] * BASE
        flags = [0] * n
        flags[1] = 1
    elif mode == "unreachable":
        old[0] = [0] * BASE
        flags = [0] + [1] * (n - 1)
    return old, flags, k


if __name__ == "__main__":
    rows, terminal, offset = generate(int(sys.argv[1]), sys.argv[2])
    print(offset)
    print(len(rows))
    print(*terminal)
    for row in rows:
        print(*(target + 1 for target in row))
