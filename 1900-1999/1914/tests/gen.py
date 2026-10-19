"""seed mode:1 zero,2 identity,3 negative unit,4 dense unit,5 swapped dense unit,
6 random,7 singular dense,8 huge diagonal,9 Hadamard,10 delayed prime rejection,
11 inconsistent modular signs,12 rank one,13 near cancellation,14 row permutation.
"""

import random
import sys

MAX_SIZE = 100
ENTRY_BOUND = 100
ZERO = 1
IDENTITY = 2
NEGATIVE_UNIT = 3
DENSE_UNIT = 4
SWAPPED_UNIT = 5
RANDOM = 6
SINGULAR = 7
DIAGONAL = 8
HADAMARD = 9
DELAYED = 10
MIXED_SIGNS = 11
RANK_ONE = 12
CANCELLATION = 13
PERMUTATION = 14
HADAMARD_SIZE = 64
ROW_OPERATIONS = 12000
FIRST_PRIME = 1000000007
SECOND_PRIME = 1000000009
DELAY_PRIMES = (
    1000000007,
    1000000009,
    1000000021,
    1000000033,
    1000000087,
    1000000093,
    1000000097,
    1000000103,
    1000000123,
    1000000181,
)


def identity(size):
    return [[int(row == column) for column in range(size)] for row in range(size)]


def dense_unit(size, rng):
    matrix = identity(size)
    for _ in range(ROW_OPERATIONS):
        target, source = rng.sample(range(size), 2)
        sign = rng.choice((-1, 1))
        candidate = [a + sign * b for a, b in zip(matrix[target], matrix[source])]
        if all(abs(value) <= ENTRY_BOUND for value in candidate):
            matrix[target] = candidate
    return matrix


def prescribed_determinant(value, size=MAX_SIZE):
    digits = []
    while value:
        digits.append(value % ENTRY_BOUND)
        value //= ENTRY_BOUND
    count = len(digits)
    matrix = identity(size)
    for row in range(count):
        matrix[row][:count] = [0] * count
    for row in range(count - 1):
        matrix[row][row] = ENTRY_BOUND
        matrix[row][row + 1] = -1
    matrix[count - 1][:count] = digits
    return matrix


def make_case(seed, mode):
    rng = random.Random(seed)
    if mode == ZERO:
        return [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    matrix = identity(MAX_SIZE)
    if mode == IDENTITY:
        pass
    elif mode == NEGATIVE_UNIT:
        matrix[0][0] = -1
    elif mode in (DENSE_UNIT, SWAPPED_UNIT, SINGULAR):
        matrix = dense_unit(MAX_SIZE, rng)
        if mode == SWAPPED_UNIT:
            matrix[0], matrix[-1] = matrix[-1], matrix[0]
        elif mode == SINGULAR:
            matrix[0] = matrix[-1][:]
    elif mode == RANDOM:
        matrix = [
            [rng.randint(-ENTRY_BOUND, ENTRY_BOUND) for _ in range(MAX_SIZE)]
            for _ in range(MAX_SIZE)
        ]
    elif mode == DIAGONAL:
        for row in range(MAX_SIZE):
            matrix[row][row] = ENTRY_BOUND
    elif mode == HADAMARD:
        for row in range(HADAMARD_SIZE):
            for column in range(HADAMARD_SIZE):
                parity = bin(row & column).count("1") % 2
                matrix[row][column] = ENTRY_BOUND * (1 if parity == 0 else -1)
    elif mode == DELAYED:
        determinant = 1
        for prime in DELAY_PRIMES:
            determinant *= prime
        matrix = prescribed_determinant(determinant + 1)
    elif mode == MIXED_SIGNS:
        # Residues +1 and -1 must not be combined into a false unit decision.
        multiple = (-2 * pow(FIRST_PRIME, -1, SECOND_PRIME)) % SECOND_PRIME
        matrix = prescribed_determinant(1 + FIRST_PRIME * multiple)
    elif mode == RANK_ONE:
        matrix = [
            [rng.choice((-ENTRY_BOUND, ENTRY_BOUND))] * MAX_SIZE
            for _ in range(MAX_SIZE)
        ]
    elif mode == CANCELLATION:
        for row in range(0, MAX_SIZE, 2):
            matrix[row][row] = ENTRY_BOUND
            matrix[row][row + 1] = ENTRY_BOUND - 1
            matrix[row + 1][row] = ENTRY_BOUND - 1
            matrix[row + 1][row + 1] = ENTRY_BOUND - 2
    elif mode == PERMUTATION:
        rng.shuffle(matrix)
    else:
        raise ValueError("unknown generator mode")
    return matrix


def main():
    matrix = make_case(int(sys.argv[1]), int(sys.argv[2]))
    print(len(matrix))
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
