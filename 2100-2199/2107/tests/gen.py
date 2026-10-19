"""Generate deterministic inputs with at most one completed function."""

import itertools
import random
import sys

from checker import completion_count

MAX_N = 35
MAX_K = 1_000_000_000
SMALL_N = 7
PAIR_CYCLE = 25
FIRST_PAIR = 12
PRIME_CYCLE = 7
FIRST_SHORT_PATH = 2
SECOND_SHORT_PATH = 3
MAX_PATH = 8
SEARCH_ATTEMPTS = 200
DUPLICATE_NODES = 2
BAD_CYCLE = 3
FALLBACK_PAIRS = 16
PERIODS = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 18, 20, 24, 30, MAX_K - 1, MAX_K)
PACKING_PERIODS = (4, 6, 8, 10, 12, 15, 18, 20, 24, 30, MAX_K - 1)
ARGUMENT_COUNT = 3


def paths(rng, lengths):
    nodes = list(range(MAX_N))
    rng.shuffle(nodes)
    partial = list(range(1, MAX_N + 1))
    offset = 0
    for length in lengths:
        chain = nodes[offset : offset + length]
        for left, right in zip(chain, chain[1:]):
            partial[left] = right + 1
        partial[chain[-1]] = 0
        offset += length
    return partial


def valid_permutation(rng, n, k):
    nodes = list(range(n))
    rng.shuffle(nodes)
    answer = [0] * n
    offset = 0
    while offset < n:
        allowed = [size for size in range(1, n - offset + 1) if k % size == 0]
        size = rng.choice(allowed)
        cycle = nodes[offset : offset + size]
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            answer[left] = right + 1
        offset += size
    return answer


def brute_count(n, k, partial):
    total = 0
    for answer in itertools.permutations(range(1, n + 1)):
        if any(fixed and fixed != target for fixed, target in zip(partial, answer)):
            continue
        valid = True
        seen = [False] * n
        for start in range(n):
            if seen[start]:
                continue
            current = start
            length = 0
            while not seen[current]:
                seen[current] = True
                length += 1
                current = answer[current] - 1
            if k % length:
                valid = False
                break
        if valid:
            total += 1
            if total == 2:
                break
    return total


def small(rng):
    n = rng.randint(2, SMALL_N)
    k = rng.choice(PERIODS)
    positive = rng.randrange(2)
    while True:
        if positive:
            partial = valid_permutation(rng, n, k)
            for index in range(n):
                if rng.randrange(2):
                    partial[index] = 0
        else:
            partial = [rng.randrange(n + 1) for _ in range(n)]
        if brute_count(n, k, partial) == positive:
            return n, k, partial


def generate(mode, seed):
    rng = random.Random(seed)
    n = MAX_N
    k = MAX_K
    if mode == "small":
        return small(rng)
    if mode == "identity":
        k = 1
        partial = [index + 1 if rng.randrange(2) else 0 for index in range(n)]
    elif mode == "specified":
        k = rng.choice(PERIODS)
        partial = list(range(1, n + 1))
        rng.shuffle(partial)
    elif mode in ("missing", "max-k"):
        if mode == "missing":
            k = rng.choice(PERIODS)
        partial = valid_permutation(rng, n, k)
        partial[rng.randrange(n)] = 0
    elif mode == "duplicate":
        partial = [0] * n
        first, second = rng.sample(range(n), DUPLICATE_NODES)
        partial[first] = partial[second] = rng.randint(1, n)
    elif mode == "bad-cycle":
        partial = [0] * n
        cycle = rng.sample(range(n), BAD_CYCLE)
        for left, right in zip(cycle, cycle[1:] + cycle[:1]):
            partial[left] = right + 1
    elif mode == "long-path":
        k = MAX_N if seed % 2 == 0 else MAX_K
        partial = paths(rng, [n])
    elif mode == "pair":
        partial = paths(rng, [FIRST_PAIR, PAIR_CYCLE - FIRST_PAIR])
    elif mode == "pairs":
        k = PRIME_CYCLE
        partial = paths(
            rng,
            [
                FIRST_SHORT_PATH,
                PRIME_CYCLE - FIRST_SHORT_PATH,
                SECOND_SHORT_PATH,
                PRIME_CYCLE - SECOND_SHORT_PATH,
            ],
        )
    elif mode == "packing-no":
        for _ in range(SEARCH_ATTEMPTS):
            k = rng.choice(PACKING_PERIODS)
            lengths = []
            remaining = n
            while remaining:
                length = 1 if remaining == 1 else rng.randint(2, min(MAX_PATH, remaining))
                lengths.append(length)
                remaining -= length
            partial = paths(rng, lengths)
            if completion_count(n, k, partial) == 0:
                break
        else:
            k = 2
            partial = paths(rng, [2] * FALLBACK_PAIRS + [BAD_CYCLE])
    else:
        raise ValueError("unknown mode: " + mode)
    return n, k, partial


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    n, k, partial = generate(sys.argv[1], int(sys.argv[2]))
    assert 1 <= n <= MAX_N and 1 <= k <= MAX_K
    assert len(partial) == n and all(0 <= target <= n for target in partial)
    assert completion_count(n, k, partial) <= 1
    print(n, k)
    print(*partial)


if __name__ == "__main__":
    main()
