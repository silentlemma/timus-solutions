import random
import sys


MAX_LENGTH = 100000
MAX_VALUE = 100000
SMALL_LENGTH = 64
SMALL_PERMUTATION_LENGTH = 256
MAX_PERIOD = 512
MAX_BLOCK = 256
SMALL_VARIANTS = ("dense", "wide", "permutation", "extremes")


def reversed_bits_order(length):
    if length <= 1:
        return list(range(1, length + 1))
    odd = reversed_bits_order((length + 1) // 2)
    even = reversed_bits_order(length // 2)
    return [2 * value - 1 for value in odd] + [2 * value for value in even]


def small_case(rng):
    length = rng.randint(1, SMALL_LENGTH)
    variant = rng.choice(SMALL_VARIANTS)
    if variant == "dense":
        bound = rng.randint(1, min(length, 10))
        return [rng.randint(1, bound) for _ in range(length)]
    if variant == "wide":
        return [rng.randint(1, MAX_VALUE) for _ in range(length)]
    if variant == "extremes":
        return [rng.choice((1, 2, MAX_VALUE - 1, MAX_VALUE)) for _ in range(length)]
    start = rng.randint(1, MAX_VALUE - length + 1)
    values = list(range(start, start + length))
    rng.shuffle(values)
    if length > 1 and rng.randrange(2):
        values[rng.randrange(length)] = rng.choice(values)
    return values


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        return small_case(rng)
    if mode == "permutation_small":
        length = rng.randint(1, SMALL_PERMUTATION_LENGTH)
        start = rng.randint(1, MAX_VALUE - length + 1)
        values = list(range(start, start + length))
        rng.shuffle(values)
        return values
    if mode == "random":
        return [rng.randint(1, MAX_VALUE) for _ in range(MAX_LENGTH)]
    if mode == "permutation":
        values = list(range(1, MAX_VALUE + 1))
        rng.shuffle(values)
        return values
    if mode == "ascending":
        return list(range(1, MAX_VALUE + 1))
    if mode == "descending":
        return list(range(MAX_VALUE, 0, -1))
    if mode == "equal":
        return [rng.randint(1, MAX_VALUE)] * MAX_LENGTH
    if mode == "alternating":
        low = rng.randint(1, MAX_VALUE - 1) if seed % 2 else 1
        high = low + 1 if seed % 2 else MAX_VALUE
        return [low if position % 2 == 0 else high for position in range(MAX_LENGTH)]
    if mode == "zigzag":
        values = []
        low = 1
        high = MAX_VALUE
        while low <= high:
            values.append(low)
            low += 1
            if low <= high:
                values.append(high)
                high -= 1
        if seed % 2:
            values.reverse()
        return values
    if mode == "periodic":
        period = rng.randint(2, MAX_PERIOD)
        start = rng.randint(1, MAX_VALUE - period + 1)
        pattern = list(range(start, start + period))
        rng.shuffle(pattern)
        return [pattern[position % period] for position in range(MAX_LENGTH)]
    if mode == "duplicate_wave":
        largest = MAX_LENGTH // 2 + 2
        start = rng.randint(0, MAX_VALUE - largest)
        values = [
            start + position // 2 + 1 + (2 if position % 2 else 0) for position in range(MAX_LENGTH)
        ]
        if seed % 2:
            values.reverse()
        return values
    if mode == "blocks":
        values = []
        start = 1
        while start <= MAX_VALUE:
            stop = min(MAX_VALUE + 1, start + rng.randint(2, MAX_BLOCK))
            block = list(range(start, stop))
            rng.shuffle(block)
            values.extend(block)
            start = stop
        return values
    if mode == "gaps":
        pattern = list(range(1, MAX_VALUE + 1, 2))
        rng.shuffle(pattern)
        return (pattern * 2)[:MAX_LENGTH]
    if mode == "recursive":
        values = reversed_bits_order(MAX_LENGTH)
        if seed % 2:
            values.reverse()
        return values
    if mode == "near_sorted":
        values = list(range(1, MAX_VALUE + 1))
        for position in range(0, MAX_LENGTH - 1, 2):
            if rng.randrange(2):
                values[position], values[position + 1] = values[position + 1], values[position]
        if seed % 2:
            values.reverse()
        return values
    raise ValueError("unknown mode: " + mode)


def main():
    mode, seed = sys.argv[1:]
    values = generate(mode, int(seed))
    sys.stdout.write(str(len(values)) + "\n")
    sys.stdout.write(" ".join(map(str, values)) + "\n")


if __name__ == "__main__":
    main()
