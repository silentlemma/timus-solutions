from itertools import product
import random
import sys

DIGIT_COUNT = 4
HEX_BASE = 16
DIGIT_BITS = 4
DOMAIN = HEX_BASE**DIGIT_COUNT
LARGE_SAMPLE = 60000


def generate(seed, mode):
    rng = random.Random(seed)
    if mode in (1, 2):
        numbers = list(range(DOMAIN))
    elif mode == 3:
        numbers = list(range(1, DOMAIN))
    elif mode == 4:
        numbers = list(range(DOMAIN - 1))
    elif mode == 5:
        numbers = rng.sample(range(DOMAIN), LARGE_SAMPLE)
    elif mode == 6:
        numbers = rng.sample(range(DOMAIN), DOMAIN // 2)
    elif mode == 7:
        fixed_digit = HEX_BASE - 2
        numbers = [
            ((first * HEX_BASE + fixed_digit) * HEX_BASE + third) * HEX_BASE + fourth
            for first, third, fourth in product(range(HEX_BASE), repeat=DIGIT_COUNT - 1)
        ]
    elif mode == 8:
        numbers = [
            number
            for number in range(DOMAIN)
            if number >> (DIGIT_BITS * (DIGIT_COUNT - 1))
            != (number >> (2 * DIGIT_BITS)) & (HEX_BASE - 1)
        ]
    else:
        numbers = [number for number in range(DOMAIN) if number & (HEX_BASE - 1)]
    if mode in (2, 4, 7, 8, 9):
        rng.shuffle(numbers)
    return numbers


def main():
    seed, mode = map(int, sys.argv[1:])
    numbers = generate(seed, mode)
    print(len(numbers))
    sys.stdout.write(
        "\n".join(f"{number:0{DIGIT_COUNT}x}" for number in numbers) + "\n"
    )


if __name__ == "__main__":
    main()
