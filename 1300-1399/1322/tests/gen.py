"""A message and what the encoder gives for it: a seed and a mode. Mode 1
gives 100000 random characters of all 53, mode 2 a short random word
repeated, mode 3 two letters, mode 4 one character repeated."""

import random
import sys

LENGTH = 100000
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"


def rotations_sorted(text):
    """Start positions of the cyclic rotations in sorted order, by
    doubling the length of the compared prefixes."""
    n = len(text)
    rank = [ord(c) for c in text]
    order = sorted(range(n), key=rank.__getitem__)
    width = 1
    while width < n:
        key = [rank[i] * (n + 200) + rank[(i + width) % n] for i in range(n)]
        order.sort(key=key.__getitem__)
        fresh = [0] * n
        for a, b in zip(order, order[1:]):
            fresh[b] = fresh[a] + (key[b] != key[a])
        rank = fresh
        if rank[order[-1]] == n - 1:
            break
        width *= 2
    return order


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        text = "".join(rng.choice(ALPHABET) for _ in range(LENGTH))
    elif mode == 2:
        word = "".join(rng.choice(ALPHABET) for _ in range(rng.randint(2, 7)))
        text = (word * LENGTH)[:LENGTH]
    elif mode == 3:
        text = "".join(rng.choice("ab") for _ in range(LENGTH))
    else:
        text = rng.choice(ALPHABET) * LENGTH
    order = rotations_sorted(text)
    print(order.index(0) + 1)
    print("".join(text[i - 1] for i in order))


main()
