"""One test from a seed and a mode: three different pile sizes, mode 1 up
to 30, mode 2 up to 10^18, mode 3 three consecutive Fibonacci numbers
in some order, which take long to settle."""

import random
import sys

FEW = 30
MOST = 10**18


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        fib = [1, 2]
        while fib[-1] + fib[-2] <= MOST:
            fib.append(fib[-1] + fib[-2])
        i = rng.randrange(len(fib) - 2)
        piles = fib[i:i + 3]
        rng.shuffle(piles)
    else:
        top = FEW if mode == 1 else MOST
        piles = set()
        while len(piles) < 3:
            piles.add(rng.randint(1, top))
        piles = list(piles)
    print(*piles)


main()
