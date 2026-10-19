import random
import sys


MAX_LENGTH = 4000
SMALL_LENGTH = 18
MAX_PERIOD = 19
MAX_SPARSE_ONES = 10


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "small":
        length = rng.randint(1, SMALL_LENGTH)
        result = "".join(rng.choice("01") for _ in range(length))
    elif mode == "random":
        length = rng.randint(1, MAX_LENGTH)
        result = "".join(rng.choice("01") for _ in range(length))
    elif mode == "max":
        result = "".join(rng.choice("01") for _ in range(MAX_LENGTH))
    elif mode == "uniform":
        result = rng.choice("01") * MAX_LENGTH
    elif mode == "alternating":
        first = rng.randrange(2)
        result = "".join(str((index + first) % 2) for index in range(MAX_LENGTH))
    elif mode == "blocks":
        split = rng.randint(1, MAX_LENGTH - 1)
        first = rng.randrange(2)
        result = str(first) * split + str(1 - first) * (MAX_LENGTH - split)
    elif mode == "sparse":
        result = [rng.choice("01")] * MAX_LENGTH
        count = rng.randint(1, MAX_SPARSE_ONES)
        for index in rng.sample(range(MAX_LENGTH), count):
            result[index] = str(1 - int(result[index]))
        result = "".join(result)
    elif mode == "periodic":
        period = rng.randint(2, MAX_PERIOD)
        pattern = "".join(rng.choice("01") for _ in range(period))
        result = (pattern * (MAX_LENGTH // period + 1))[:MAX_LENGTH]
    elif mode == "symmetric":
        left = "".join(rng.choice("01") for _ in range(MAX_LENGTH // 2))
        result = left + left[::-1]
    else:
        raise SystemExit("unknown mode")
    print(result)


if __name__ == "__main__":
    main()
