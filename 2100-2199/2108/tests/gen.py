import random
import sys

MAX_FIGURES = 1000
MAX_RULES = 4000
SMALL_FIGURES = 45
SMALL_RULES = 120
SPARSE_FIGURES = 100
SPARSE_RULES = 350
SPARSE_WIDTH = 3
DENSITIES = (0, 1, 2, 10)


def sparse_mask(rng, size, width):
    count = rng.randint(0, min(size, width))
    result = 0
    for index in rng.sample(range(size), count):
        result |= 1 << index
    return result


def random_mask(rng, size):
    density = rng.choice(DENSITIES)
    if density == 0:
        return 0
    if density == 1:
        return (1 << size) - 1
    if density == 2:
        return rng.getrandbits(size)
    result = 0
    for index in range(size):
        if rng.randrange(density) == 0:
            result |= 1 << index
    return result


def small_random(rng):
    size = rng.randint(1, SMALL_FIGURES)
    count = rng.randint(0, SMALL_RULES)
    rules = [(random_mask(rng, size), random_mask(rng, size)) for _ in range(count)]
    return size, rules, random_mask(rng, size)


def small_sparse(rng):
    size = rng.randint(1, SPARSE_FIGURES)
    count = rng.randint(0, SPARSE_RULES)
    rules = [
        (sparse_mask(rng, size, SPARSE_WIDTH), sparse_mask(rng, size, SPARSE_WIDTH))
        for _ in range(count)
    ]
    return size, rules, sparse_mask(rng, size, SPARSE_WIDTH)


def blocked(rng):
    size = rng.randint(2, SPARSE_FIGURES)
    count = rng.randint(1, SPARSE_RULES)
    missing = 1 << (size - 1)
    rules = [(random_mask(rng, size) | missing, random_mask(rng, size - 1)) for _ in range(count)]
    return size, rules, random_mask(rng, size - 1)


def cycles(rng):
    size = rng.randint(2, SPARSE_FIGURES)
    rules = [(1 << index, 1 << ((index + 1) % size)) for index in range(size)]
    count = rng.randint(size, SPARSE_RULES)
    while len(rules) < count:
        left = sparse_mask(rng, size, 2)
        right = sparse_mask(rng, size, 2)
        rules.append((left, right))
    rng.shuffle(rules)
    initial = 0 if rng.randrange(2) == 0 else 1 << rng.randrange(size)
    return size, rules, initial


def chain(rng):
    size = rng.randint(2, SPARSE_FIGURES)
    rules = [(1 << index, 1 << (index + 1)) for index in range(size - 1)]
    count = rng.randint(size - 1, SPARSE_RULES)
    while len(rules) < count:
        index = rng.randrange(size)
        rules.append((1 << index, 1 << index))
    rng.shuffle(rules)
    return size, rules, 1


def reverse_max(rng):
    size = MAX_FIGURES
    final = 1 << (size - 1)
    rules = [(final, final) for _ in range(MAX_RULES - size + 1)]
    rules.extend((1 << index, 1 << (index + 1)) for index in reversed(range(size - 1)))
    return size, rules, 1


def reverse_noop(rng):
    size = MAX_FIGURES
    rules = [(0, 1) for _ in range(MAX_RULES - size + 1)]
    rules.extend((1 << index, 1 << (index + 1)) for index in reversed(range(size - 1)))
    return size, rules, 1


def dense_inert(rng):
    size = MAX_FIGURES
    full = (1 << size) - 1
    rules = [(full, rng.getrandbits(size)) for _ in range(MAX_RULES)]
    return size, rules, 0


def dense_fire(rng):
    size = MAX_FIGURES
    full = (1 << size) - 1
    rules = [(rng.getrandbits(size), full) for _ in range(MAX_RULES)]
    return size, rules, full


def dense_chain(rng):
    size = MAX_FIGURES
    full = (1 << size) - 1
    rules = [
        (full ^ (sparse_mask(rng, size - 1, SPARSE_WIDTH) << 1), rng.getrandbits(size))
        for _ in range(MAX_RULES - size + 1)
    ]
    rules.extend((1 << index, 1 << (index - 1)) for index in range(1, size))
    return size, rules, 1 << (size - 1)


def dense_blocked(rng):
    size = MAX_FIGURES
    full = (1 << size) - 1
    rules = [(full, full ^ 1) for _ in range(MAX_RULES - size + 2)]
    rules.extend((1 << index, 1 << (index - 1)) for index in range(2, size))
    return size, rules, 1 << (size - 1)


def random_max(rng):
    size = MAX_FIGURES
    rules = [(random_mask(rng, size), random_mask(rng, size)) for _ in range(MAX_RULES)]
    return size, rules, random_mask(rng, size)


def empty_max(rng):
    size = MAX_FIGURES
    rules = [(0, rng.getrandbits(size)) for _ in range(MAX_RULES)]
    return size, rules, 0


def no_rules(rng):
    return MAX_FIGURES, [], rng.getrandbits(MAX_FIGURES)


MODES = {
    "random": small_random,
    "sparse": small_sparse,
    "blocked": blocked,
    "cycles": cycles,
    "chain": chain,
    "reverse-max": reverse_max,
    "reverse-noop": reverse_noop,
    "dense-inert": dense_inert,
    "dense-fire": dense_fire,
    "dense-chain": dense_chain,
    "dense-blocked": dense_blocked,
    "random-max": random_max,
    "empty-max": empty_max,
    "no-rules": no_rules,
}


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    size, rules, initial = MODES[mode](rng)
    lines = [f"{size} {len(rules)}"]
    for left, right in rules:
        lines.append(f"{left:0{size}b} {right:0{size}b}")
    lines.append(f"{initial:0{size}b}")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
