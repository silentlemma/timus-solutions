"""One test from a seed and a mode, about 100 KB unless small. Mode 1
mixes letters a to c with digits, mode 2 is mostly zeros, mode 3 is a few
short strings, mode 4 has numbers of up to 200 digits, mode 5 is many
very short strings. Mode 6 is a 100,000-byte pair of long numbers differing
only in the last digit. Mode 7 shuffles names with 8,000 shared letter/number
pairs and differences or padding near the end."""

import random
import sys

BUDGET = 100000 - 1000  # bytes, with room for line ends
FEW = 12
SHORT, LONG = 6, 200


def word(rng, mode):
    length = rng.randint(1, 3 if mode == 5 else (LONG if mode == 4 else SHORT * 2))
    if mode == 2:
        return "".join(rng.choice("0000a1") for _ in range(length))
    if mode == 4:
        cut = rng.randint(0, length)
        return "x" + "".join(rng.choice("0123456789") for _ in range(cut)) + "y" * rng.randint(0, 1)
    return "".join(rng.choice("abc0120") for _ in range(length))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        prefix = str(rng.randint(1, 9)) + "".join(
            rng.choice("0123456789") for _ in range(49997)
        )
        words = [prefix + "9", prefix + "8"]
        rng.shuffle(words)
        print("\n".join(words))
        return
    if mode == 7:
        prefix = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") + str(rng.randrange(10))
            for _ in range(8000)
        )
        words = [prefix + suffix for suffix in ("", "a1", "a01", "a001", "a2", "b0")]
        rng.shuffle(words)
        print("\n".join(words))
        return
    words, size = [], 0
    while True:
        w = word(rng, mode)
        if (mode == 3 and len(words) >= rng.randint(1, FEW)) or size + len(w) + 1 > BUDGET:
            break
        words.append(w)
        size += len(w) + 1
    print("\n".join(words))


main()
