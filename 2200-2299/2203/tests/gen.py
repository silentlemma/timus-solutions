import math
import random
import sys

MAX_INGREDIENT = 100
MAX_VALUE = 1_000_000_000
SMALL_INGREDIENT = 10
SMALL_PACKAGE = 30
SMALL_COUNT = 1_000
NEAR_WINDOW = 10_000
NEAR_STEP = 3


def generate(mode, rng, seed):
    a = rng.randint(1, MAX_INGREDIENT)
    b = rng.randint(1, MAX_INGREDIENT)
    n = rng.randint(1, MAX_VALUE)

    if mode == "small":
        a = rng.randint(1, SMALL_INGREDIENT)
        b = rng.randint(1, SMALL_INGREDIENT)
        x = rng.randint(1, SMALL_PACKAGE)
        y = rng.randint(1, SMALL_PACKAGE)
        n = rng.randint(1, SMALL_COUNT)
    elif mode == "random":
        sizes = (MAX_INGREDIENT, MAX_INGREDIENT**2, MAX_VALUE)
        x = rng.randint(1, rng.choice(sizes))
        y = rng.randint(1, rng.choice(sizes))
    elif mode == "always":
        x = rng.randint(1, MAX_VALUE)
        y = rng.randint(1, MAX_VALUE)
        if seed % 2 == 0:
            x = rng.randint(1, a)
        else:
            y = rng.randint(1, b)
    elif mode == "rounding":
        quotient = rng.randint(1, MAX_VALUE // max(a, b))
        x = min(MAX_VALUE, max(1, a * quotient + rng.randint(-1, 1)))
        y = min(MAX_VALUE, max(1, b * quotient + rng.randint(-1, 1)))
        n = min(MAX_VALUE, quotient + rng.randint(-1, 1))
        n = max(1, n)
    elif mode == "coprime":
        a = rng.randint(MAX_INGREDIENT // 2, MAX_INGREDIENT)
        b = rng.randint(MAX_INGREDIENT // 2, MAX_INGREDIENT)
        x = rng.randint(MAX_VALUE - NEAR_WINDOW, MAX_VALUE)
        y = rng.randint(MAX_VALUE - NEAR_WINDOW, MAX_VALUE)
        while math.gcd(x, y) != 1:
            y = rng.randint(MAX_VALUE - NEAR_WINDOW, MAX_VALUE)
        n = MAX_VALUE
    elif mode == "gcd":
        divisor = rng.randint(2, MAX_INGREDIENT)
        x = divisor * rng.randint(1, MAX_VALUE // divisor)
        y = divisor * rng.randint(1, MAX_VALUE // divisor)
        n = MAX_VALUE
    elif mode == "reduced":
        numerator = rng.randint(1, SMALL_INGREDIENT)
        first_scale = rng.randint(1, MAX_INGREDIENT // numerator)
        second_scale = rng.randint(1, MAX_INGREDIENT // numerator)
        denominator = rng.randint(numerator + 1, MAX_VALUE // max(first_scale, second_scale))
        a = numerator * first_scale
        b = numerator * second_scale
        x = denominator * first_scale
        y = denominator * second_scale
        n = MAX_VALUE
    elif mode == "dense":
        x = a + rng.randint(0, NEAR_STEP)
        y = b + rng.randint(0, NEAR_STEP)
        n = MAX_VALUE
    elif mode == "max":
        a = MAX_INGREDIENT
        b = MAX_INGREDIENT
        x = MAX_VALUE
        y = MAX_VALUE - seed % 2
        n = MAX_VALUE
    else:
        raise ValueError("unknown mode: " + mode)

    return a, b, x, y, n


def main():
    mode, seed_text = sys.argv[1:]
    seed = int(seed_text)
    print(*generate(mode, random.Random(seed), seed))


if __name__ == "__main__":
    main()
