"""Generate permutations: small/medium random, or maximum-size structured cases.

Modes 1/2 are random, 3 is maximum random, 4/5 are monotone, 6 is balanced,
7 alternates extrema, 8 peels alternating boundaries, 9 shuffles blocks,
10 nearly follows a chain, 11 is variable balanced, and 12 uses variable blocks.
"""

import random
import sys

SMALL_RANDOM = 1
MEDIUM_RANDOM = 2
MAX_RANDOM = 3
MAX_ASCENDING = 4
MAX_DESCENDING = 5
MAX_BALANCED = 6
MAX_EXTREMA = 7
MAX_BOUNDARY_CHAIN = 8
MAX_BLOCKS = 9
MAX_NEAR_CHAIN = 10
VARIABLE_BALANCED = 11
VARIABLE_BLOCKS = 12

MAX_SIZE = 100_000
SMALL_LIMIT = 12
MEDIUM_MINIMUM = 100
MEDIUM_LIMIT = 2_000
VARIABLE_LIMIT = 3_000
BLOCK_SIZE = 257
SWAP_COUNT = 256


def balanced(size, rng):
    values = [0] * size
    pending = [(0, size)]
    value = 1
    while pending:
        left, right = pending.pop()
        middle = (left + right) // 2
        values[middle] = value
        value += 1
        children = []
        if left < middle:
            children.append((left, middle))
        if middle + 1 < right:
            children.append((middle + 1, right))
        if rng.randrange(2):
            children.reverse()
        pending.extend(children)
    return values


def blocks(size, rng):
    values = []
    for start in range(1, size + 1, BLOCK_SIZE):
        block = list(range(start, min(start + BLOCK_SIZE, size + 1)))
        rng.shuffle(block)
        values.extend(block)
    return values


def generate(mode, seed):
    rng = random.Random(seed)
    size = MAX_SIZE
    if mode == SMALL_RANDOM:
        size = rng.randint(1, SMALL_LIMIT)
    elif mode == MEDIUM_RANDOM:
        size = rng.randint(MEDIUM_MINIMUM, MEDIUM_LIMIT)
    elif mode in (VARIABLE_BALANCED, VARIABLE_BLOCKS):
        size = rng.randint(1, VARIABLE_LIMIT)

    if mode in (SMALL_RANDOM, MEDIUM_RANDOM, MAX_RANDOM):
        values = list(range(1, size + 1))
        rng.shuffle(values)
        return values
    if mode == MAX_ASCENDING:
        return list(range(1, size + 1))
    if mode == MAX_DESCENDING:
        return list(range(size, 0, -1))
    if mode in (MAX_BALANCED, VARIABLE_BALANCED):
        return balanced(size, rng)
    if mode == MAX_EXTREMA:
        values = []
        left, right = 1, size
        while left <= right:
            values.append(left)
            left += 1
            if left <= right:
                values.append(right)
                right -= 1
        return values
    if mode == MAX_BOUNDARY_CHAIN:
        values = [0] * size
        left, right = 0, size - 1
        for value in range(1, size + 1):
            if value % 2:
                values[left] = value
                left += 1
            else:
                values[right] = value
                right -= 1
        return values
    if mode in (MAX_BLOCKS, VARIABLE_BLOCKS):
        return blocks(size, rng)
    if mode == MAX_NEAR_CHAIN:
        values = list(range(1, size + 1))
        for _ in range(SWAP_COUNT):
            index = rng.randrange(size - 1)
            values[index], values[index + 1] = values[index + 1], values[index]
        return values
    raise ValueError("unknown generator mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    values = generate(mode, seed)
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
