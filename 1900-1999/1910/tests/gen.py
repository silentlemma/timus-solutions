import random
import sys

MAX_COUNT = 1000
MAX_VALUE = 1000000
WINDOW_SIZE = 3


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    if mode in (1, 2):
        count = randomizer.randint(WINDOW_SIZE, 20) if mode == 1 else MAX_COUNT
        bound = 50 if mode == 1 else MAX_VALUE
        while True:
            values = [randomizer.randint(1, bound) for _ in range(count)]
            sums = [
                sum(values[start : start + WINDOW_SIZE]) for start in range(count - 2)
            ]
            if sums.count(max(sums)) == 1:
                break
    elif mode in (3, 4, 5):
        values = [1] * MAX_COUNT
        start = (
            0
            if mode == 3
            else MAX_COUNT - WINDOW_SIZE
            if mode == 4
            else MAX_COUNT // 2 - 2
        )
        values[start : start + WINDOW_SIZE] = [MAX_VALUE] * WINDOW_SIZE
    elif mode == 6:
        values = list(range(1, MAX_COUNT + 1))
    elif mode == 7:
        values = list(range(MAX_COUNT, 0, -1))
    else:
        values = [randomizer.randint(1, MAX_VALUE) for _ in range(WINDOW_SIZE)]
    assert WINDOW_SIZE <= len(values) <= MAX_COUNT and all(
        1 <= value <= MAX_VALUE for value in values
    )
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
