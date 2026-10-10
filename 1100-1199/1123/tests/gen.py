"""Random salaries: a seed, the number of digits and a mode. Mode 0 draws
any digits, mode 1 ends the left half (with its middle digit) in a block of
nines and makes the right half beat its mirror just past that block, so
that adding one to the left half carries through all the nines; mode 2 is
a palindrome already."""

import random
import sys

BLOCK = 3


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    digits = [rng.choice("123456789")] + [rng.choice("0123456789") for _ in range(n - 1)]
    half = (n + 1) // 2
    if mode == 1:
        nines = rng.randint(1, max(1, half // BLOCK))
        for k in range(half - nines, half):
            digits[k] = "9"
        if digits[half - nines - 1] == "9":
            digits[half - nines - 1] = "8"
        # copy the mirror over the nines, then beat it at the next digit
        j = half
        while j < n and digits[n - 1 - j] == "9":
            digits[j] = "9"
            j += 1
        if j < n:
            digits[j] = str(rng.randint(int(digits[n - 1 - j]) + 1, 9))
    elif mode == 2:
        for k in range(n // 2):
            digits[n - 1 - k] = digits[k]
    sys.stdout.write("".join(digits) + "\n")


if __name__ == "__main__":
    main()
