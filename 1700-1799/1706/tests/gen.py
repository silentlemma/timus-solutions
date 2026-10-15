"""One test from a seed and a mode: mode 1 a short random string, mode 2
the largest sizes with all letters, mode 3 the largest sizes with two
letters, mode 4 the largest sizes with a short repeated block,
mode 5 random long runs with n = 4000 and k = 17, mode 6 a random
odd palindrome with n = 61 and k = 60."""

import random
import sys

MOST_N = 4000
MOST_K = 1000
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, 60)
        k = rng.randint(1, n - 1)
        s = "".join(rng.choice("abc") for _ in range(n))
    elif mode in (2, 3):
        n, k = MOST_N, MOST_K
        letters = LETTERS if mode == 2 else "ab"
        s = "".join(rng.choice(letters) for _ in range(n))
    elif mode == 5:
        n, k = MOST_N, 17
        runs = []
        length = 0
        previous = ""
        while length < n:
            letter = rng.choice("".join(c for c in "abz" if c != previous))
            run = letter * rng.randint(18, 80)
            runs.append(run)
            length += len(run)
            previous = letter
        s = "".join(runs)[:n]
    elif mode == 6:
        n, k = 61, 60
        half = "".join(rng.choice("abcd") for _ in range(n // 2))
        s = half + rng.choice("abcd") + half[::-1]
    else:
        n, k = MOST_N, MOST_K
        block = "".join(rng.choice("ab") for _ in range(rng.randint(2, 30)))
        s = (block * n)[:n]
        s = s[:n // 2] + rng.choice("ab") + s[n // 2 + 1:]
    print(k)
    print(s)


main()
