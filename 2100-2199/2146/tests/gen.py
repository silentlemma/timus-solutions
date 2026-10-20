"""Drum from "MODE SEED": mode 1 a short drum over three letters, mode 2
10^5 random letters, mode 3 a periodic drum of length 83160 (many
divisors) with some letters spoiled, mode 4 10^5 equal letters, mode 5
83160 random letters and no changes, so every divisor is tried."""

import random
import sys

MAX_N = 10 ** 5
RICH_N = 83160
SMALL_N = 6
FEW = "abc"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
SPOILED = 50


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        s = [rng.choice(FEW) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        s = [rng.choice(ALPHABET) for _ in range(n)]
    elif mode == 3:
        n = RICH_N
        divisors = [d for d in range(1, n + 1) if n % d == 0]
        d = rng.choice(divisors[:len(divisors) // 2])
        block = [rng.choice(ALPHABET) for _ in range(d)]
        s = block * (n // d)
        for i in rng.sample(range(n), SPOILED):
            s[i] = rng.choice(ALPHABET)
    elif mode == 4:
        n = MAX_N
        s = ["z"] * n
    else:
        n = RICH_N
        s = [rng.choice(ALPHABET) for _ in range(n)]
    if mode == 3:
        k = rng.randint(0, 2 * SPOILED)
    else:
        k = 0 if mode == 5 else rng.randint(0, n)
    print(n, k)
    print("".join(s))


main()
