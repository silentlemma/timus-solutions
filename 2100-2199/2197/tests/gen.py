"""Generate one valid input: python gen.py MODE SEED.

Modes: 1 small, 2 periodic, 3 overlaps, 4 maximum point updates,
5 whole copies, 6 maximum dictionary, 7 prime length, 8 composite length,
9 longest unused string, 10 many fragments, 11 maximum source, 12 nested copies,
13 many prime factors with a maximum dictionary, 14 sparse damage at that size.
"""

import random
import string
import sys

N_LIMIT = 200000
STRING_LIMIT = 1000000
COMPOSITE_LENGTH = 166320
MANY_PRIMES_LENGTH = 180180
SMALL_N = 96
SMALL_M = 12
SMALL_Q = 50
OVERLAP_N = 128
OVERLAP_Q = 100
PERIOD_LIMIT = 8
PERIODIC_Q = 80
SHORT_LENGTH = 5
NESTED_COUNT = 20
ALPHABET = string.ascii_lowercase

SMALL = 1
PERIODIC = 2
OVERLAPS = 3
POINTS = 4
COPIES = 5
DICTIONARY = 6
PRIME = 7
COMPOSITE = 8
UNUSED = 9
FRAGMENTS = 10
SOURCE = 11
NESTED = 12
COMPOSITE_DICTIONARY = 13
SPARSE_DICTIONARY = 14


def generate(mode, seed):
    rng = random.Random(seed)

    def word(length, alphabet=ALPHABET):
        return "".join(rng.choices(alphabet, k=length))

    def repeat(root, length):
        return (root * ((length + len(root) - 1) // len(root)))[:length]

    if mode in (SMALL, PERIODIC, OVERLAPS):
        limit = OVERLAP_N if mode == OVERLAPS else SMALL_N
        n = rng.randint(1, limit)
        initial = word(n, ALPHABET[: rng.randint(1, len(ALPHABET))])
        bank = [word(rng.randint(1, n * 2)) for _ in range(rng.randint(0, SMALL_M))]
        count = rng.randint(0, SMALL_Q)
        if mode == PERIODIC:
            period = rng.randint(1, PERIOD_LIMIT)
            n = period * rng.randint(1, SMALL_N // period)
            initial = repeat(word(period), n)
            bank = ["a", "b", initial, "a" * n, repeat("ab", n)]
            bank += [initial[: rng.randint(1, n)] for _ in range(SMALL_M)]
            count = PERIODIC_Q
        elif mode == OVERLAPS:
            bank += ["z", "a" * n, word(max(1, n // 2))]
            count = OVERLAP_Q
        usable = [i for i, text in enumerate(bank, 1) if len(text) <= n]
        queries = []
        if usable:
            for step in range(count):
                index = rng.choice(usable)
                last = n - len(bank[index - 1]) + 1
                position = rng.choice([1, last, rng.randint(1, last)])
                queries.append((position, index))
        return n, initial, bank, queries

    n = N_LIMIT
    if mode == POINTS:
        bank = list(ALPHABET) + [word(STRING_LIMIT - len(ALPHABET))]
        queries = [(rng.randint(1, n), rng.randint(1, len(ALPHABET))) for _ in range(N_LIMIT)]
        return n, word(n), bank, queries
    if mode == COPIES:
        bank = ["a" * n, repeat("ab", n), repeat("abcde", n), word(n), "z" * n]
        queries = [(1, step % len(bank) + 1) for step in range(N_LIMIT)]
        return n, repeat("abcde", n), bank, queries
    if mode in (DICTIONARY, COMPOSITE_DICTIONARY, SPARSE_DICTIONARY):
        if mode != DICTIONARY:
            n = MANY_PRIMES_LENGTH
        if mode == SPARSE_DICTIONARY:
            bank = ["a" * (SHORT_LENGTH - 1) + rng.choice("ab") for _ in range(N_LIMIT)]
        else:
            bank = [word(SHORT_LENGTH) for _ in range(N_LIMIT)]
        queries = [(rng.randint(1, n - SHORT_LENGTH + 1), index + 1) for index in range(N_LIMIT)]
        initial = "a" * n if mode == SPARSE_DICTIONARY else word(n)
        return n, initial, bank, queries
    if mode == PRIME:
        n -= 1
        while any(n % divisor == 0 for divisor in range(2, int(n**0.5) + 1)):
            n -= 1
        bank = ["a", "b", "a" * (n // 2), word(n // 2), word(n)]
        queries = []
        for _ in range(N_LIMIT):
            index = rng.randint(1, len(bank))
            queries.append((rng.randint(1, n - len(bank[index - 1]) + 1), index))
        return n, "a" * n, bank, queries
    if mode == COMPOSITE:
        n = COMPOSITE_LENGTH
        queries = []
        for _ in range(N_LIMIT // 2):
            position = rng.randint(1, n)
            queries.extend([(position, 2), (position, 1)])
        return n, "a" * n, ["a", "b"], queries
    if mode == UNUSED:
        return 1, "z", [word(STRING_LIMIT)], []
    if mode == FRAGMENTS:
        bank = ["b", "a" * n]
        queries = [(step * 2 + 1, 1) for step in range(n // 2)]
        queries += [(1, 2)] * (N_LIMIT - len(queries))
        return n, "a" * n, bank, queries
    if mode == SOURCE:
        return n, word(n), [word(STRING_LIMIT)], []
    if mode == NESTED:
        bank = []
        length = n
        for index in range(NESTED_COUNT):
            bank.append(repeat("ab" if index % 2 else "z", length))
            length = max(1, length // 2)
        queries = []
        for step in range(N_LIMIT):
            index = rng.randint(1, len(bank))
            last = n - len(bank[index - 1]) + 1
            queries.append((1 if step % 2 else last, index))
        return n, word(n), bank, queries
    raise ValueError("unknown mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    n, initial, bank, queries = generate(mode, seed)
    lines = [f"{n} {len(bank)} {len(queries)}", initial]
    lines.extend(bank)
    lines.extend(f"{position} {index}" for position, index in queries)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
