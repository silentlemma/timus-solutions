"""Usage: gen.py SEED MODE.

Modes: insert,shorten,prefix,delete,pairs,alphabet,largest,high,hidden,one,mixed,random.
Every input has nonempty strings of length at most 100000 and cannot end empty.
"""

from collections import Counter
import random
import sys

LIMIT = 100000
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def generate(seed, mode):
    alphabet = (ALPHABET * (LIMIT // len(ALPHABET) + 1))[:LIMIT]
    if mode == "insert":
        return "b" * LIMIT, "a" * LIMIT
    if mode == "shorten":
        return "a" * LIMIT, "a" * (LIMIT - 1)
    if mode == "prefix":
        return "a" * (LIMIT - 1) + "b", "a" * LIMIT
    if mode == "delete":
        return "z" * (LIMIT - 1) + "a", "z" * LIMIT
    if mode == "pairs":
        return "za" * (LIMIT // 2), "z" * LIMIT
    if mode == "alphabet":
        return alphabet, "a" * LIMIT
    if mode == "largest":
        return alphabet, "z" * LIMIT
    if mode == "high":
        return "z" * LIMIT, "y" * LIMIT
    if mode == "hidden":
        return "z" * (LIMIT - len(ALPHABET)) + ALPHABET, "y" * LIMIT
    if mode == "one":
        return "z" * LIMIT, "z"
    if mode == "mixed":
        return "zy" * (LIMIT // 2), "x" * LIMIT
    if mode != "random":
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    source = "".join(rng.choices(ALPHABET, k=LIMIT))
    modifiers = "".join(rng.choices(ALPHABET, k=LIMIT))
    if Counter(source) == Counter(modifiers):
        replacement = "b" if modifiers[0] == "a" else "a"
        modifiers = replacement + modifiers[1:]
    return source, modifiers


if __name__ == "__main__":
    print("\n".join(generate(int(sys.argv[1]), sys.argv[2])))
