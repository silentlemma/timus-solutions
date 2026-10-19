import random
import sys

MAX_COUNT = 100000
MAX_VALUE = 1000000000
BLOCK_LENGTH = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        values = list(range(1, MAX_COUNT + 1))
    elif mode == 2:
        values = list(range(MAX_COUNT, 0, -1))
    elif mode == 3:
        values = [MAX_VALUE, 1] + list(range(2, MAX_COUNT))
    elif mode == 4:
        values = [2] + list(range(3, MAX_COUNT + 1)) + [1]
    elif mode == 5:
        values = rng.sample(range(1, MAX_VALUE + 1), MAX_COUNT)
    elif mode in (6, 7):
        values = list(range(2, MAX_COUNT + 2))
        index = MAX_COUNT // 2 if mode == 6 else MAX_COUNT // 2 - 1
        values[index] = 1
    elif mode == 8:
        values = list(range(2 * MAX_COUNT, 3 * MAX_COUNT))
        for index in range(0, MAX_COUNT, BLOCK_LENGTH):
            values[index] = MAX_COUNT - index
    else:
        values = list(range(MAX_VALUE - MAX_COUNT + 1, MAX_VALUE + 1))
        rng.shuffle(values)
    return values


def main():
    seed, mode = map(int, sys.argv[1:])
    values = generate(seed, mode)
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
