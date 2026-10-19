import random
import sys

MAX_FIRST = 10**12
MAX_LIMIT = 10**18


def main():
    randomizer = random.Random(int(sys.argv[1]))
    mode = int(sys.argv[2])
    if mode == 1:
        first, limit = randomizer.randint(1, 1000), randomizer.randint(1, 10000)
    elif mode == 2:
        first, limit = 999999999989, MAX_LIMIT
    elif mode == 3:
        first, limit = 100280245065, MAX_LIMIT
    elif mode == 4:
        first, limit = 200560490130, MAX_LIMIT - 1
    elif mode == 5:
        first, limit = 999983**2, MAX_LIMIT
    elif mode == 6:
        first, limit = 2**39, MAX_LIMIT - 1
    elif mode == 7:
        first, limit = 3**25, MAX_LIMIT - 1
    elif mode == 8:
        first, limit = 1, MAX_LIMIT
    elif mode == 9:
        first, limit = MAX_FIRST, MAX_LIMIT
    elif mode == 10:
        first, limit = 999983 * 999979, MAX_LIMIT
    elif mode == 11:
        first = 1
        for prime in (2, 3, 5, 7, 11, 13):
            for _ in range(randomizer.randrange(5)):
                if first * prime <= MAX_FIRST:
                    first *= prime
        limit = randomizer.randint(1, MAX_LIMIT)
    else:
        first, limit = (
            randomizer.randint(1, MAX_FIRST),
            randomizer.randint(1, MAX_LIMIT),
        )
    print(first, limit)


if __name__ == "__main__":
    main()
