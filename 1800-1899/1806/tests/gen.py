"""One test from a seed and a mode: n fighters and costs falling with
the common prefix. Mode 1 a few fighters whose numbers use few digits,
mode 2 50000 fighters with the last five digits free, so most numbers
have many neighbours, mode 3 50000 fighters with any numbers, mode 4 a
long chain of single changes from the first fighter to the last, mode
5 the dense case of mode 2 with Chapaev far away from everyone."""

import random
import sys

DIGITS = 10
LIMIT = 50000
TOP = 10000
FEW = 12
FREE = 5


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    cost = sorted((rng.randint(1, TOP) for _ in range(DIGITS)), reverse=True)
    numbers = set()
    if mode == 1:
        n = rng.randint(2, FEW)
        letters = "0123456789"[:rng.randint(2, 3)]
        while len(numbers) < n:
            numbers.add("".join(rng.choice(letters) for _ in range(DIGITS)))
        numbers = list(numbers)
    elif mode in (2, 3, 5):
        n = LIMIT
        head = "".join(rng.choice("0123456789") for _ in range(DIGITS - FREE))
        while len(numbers) < n:
            if mode != 3:
                tail = "".join(rng.choice("0123456789") for _ in range(FREE))
                numbers.add(head + tail)
            else:
                numbers.add("".join(rng.choice("0123456789") for _ in range(DIGITS)))
        numbers = list(numbers)
    else:
        current = [rng.choice("0123456789") for _ in range(DIGITS)]
        chain = ["".join(current)]
        seen = {chain[0]}
        while len(chain) < LIMIT // 10:
            p = rng.randrange(DIGITS)
            current[p] = rng.choice("0123456789")
            s = "".join(current)
            if s not in seen:
                seen.add(s)
                chain.append(s)
        numbers = chain
    if mode != 4:
        rng.shuffle(numbers)
    if mode == 5:
        # a number differing from the common head in every digit
        last = numbers[-1]
        shifted = "".join(str((int(ch) + 1) % DIGITS) for ch in last[:DIGITS - FREE])
        numbers[-1] = shifted + last[DIGITS - FREE:]
    print(len(numbers))
    print(*cost)
    print("\n".join(numbers))


main()
