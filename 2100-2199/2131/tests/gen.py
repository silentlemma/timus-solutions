"""Generate distinct team names from a mode and a seed.

Modes 1 and 2 are small random and structured cases. Mode 3 is one maximal
random name; mode 4 is a maximal unary pair; mode 5 has many short names.
Modes 6 and 7 use long periodic names and a positive substring, respectively.
Mode 8 is medium random input; mode 9 is a maximal pair of random names.
Modes 10 and 11 are maximal all-positive inputs with random and shared cores.
Mode 12 maximizes the number of distinct names within the total length limit.
"""

import itertools
import random
import string
import sys

MAX_TOTAL = 200_000
SMALL_NAMES = 12
SMALL_LENGTH = 12
STRUCTURED_NAMES = 16
STRUCTURED_LENGTH = 40
MEDIUM_NAMES = 60
MEDIUM_LENGTH = 80
SHORT_LENGTH = 4
PERIODIC_NAMES = 5
POSITIVE_NAMES = 400
POSITIVE_LENGTH = MAX_TOTAL // POSITIVE_NAMES
PERIOD = "abac_"
ALPHABET = string.ascii_lowercase + "_"
SMALL_ALPHABET = "abc_"
BINARY_ALPHABET = "ab"
MODE_SINGLE = 3
MODE_UNARY = 4
MODE_SHORT = 5
MODE_PERIODIC = 6
MODE_WINDOW = 7
MODE_MEDIUM = 8
MODE_PAIR = 9
MODE_POSITIVE_RANDOM = 10
MODE_POSITIVE_SHARED = 11
MODE_MAX_COUNT = 12


def random_name(rng, length, alphabet):
    return "".join(rng.choices(alphabet, k=length))


def random_teams(rng, count, limit, alphabet):
    teams = []
    used = set()
    while len(teams) < count:
        name = random_name(rng, rng.randint(1, limit), alphabet)
        if name not in used:
            used.add(name)
            teams.append((name, not teams or bool(rng.randrange(2))))
    return teams


def encoded_name(value):
    chars = []
    for _ in range(SHORT_LENGTH):
        chars.append(ALPHABET[value % len(ALPHABET)])
        value //= len(ALPHABET)
    return "".join(chars)


def structured_teams(rng):
    length = rng.randint(SMALL_LENGTH, STRUCTURED_LENGTH)
    period = random_name(rng, rng.randint(1, SHORT_LENGTH), SMALL_ALPHABET)
    base = (period * length)[:length]
    teams = [(base, True)]
    used = {base}
    count = rng.randint(2, STRUCTURED_NAMES)
    while len(teams) < count:
        left = rng.randrange(length)
        right = rng.randrange(left + 1, length + 1)
        name = base[left:right]
        if rng.randrange(2):
            name = rng.choice(ALPHABET) + name + rng.choice(ALPHABET)
        if name not in used:
            used.add(name)
            teams.append((name, bool(rng.randrange(2))))
    return teams


def generate(mode, rng):
    if mode == 1:
        return random_teams(rng, rng.randint(1, SMALL_NAMES), SMALL_LENGTH, SMALL_ALPHABET)
    if mode == 2:
        return structured_teams(rng)
    if mode == MODE_SINGLE:
        return [(random_name(rng, MAX_TOTAL, ALPHABET), True)]
    if mode == MODE_UNARY:
        length = MAX_TOTAL // 2
        return [("a" * length, True), ("a" * (length - 1) + "b", False)]
    if mode == MODE_SHORT:
        alphabet = list(ALPHABET)
        rng.shuffle(alphabet)
        base = "".join(alphabet)
        count, remainder = divmod(MAX_TOTAL - len(base), SHORT_LENGTH)
        values = rng.sample(range(len(ALPHABET) ** SHORT_LENGTH), count)
        teams = [(base, True)]
        teams.extend((encoded_name(value), False) for value in values)
        if remainder:
            teams.append(("a" * remainder, False))
        return teams
    if mode == MODE_PERIODIC:
        length = MAX_TOTAL // PERIODIC_NAMES
        base = (PERIOD * length)[:length]
        return [
            (base, True),
            (base[1:] + "d", True),
            ("e" + base[:-1], False),
            (base[:-1] + "f", True),
            ("g" + base[1:], False),
        ]
    if mode == MODE_WINDOW:
        length = MAX_TOTAL // 2
        base = random_name(rng, length, BINARY_ALPHABET)
        half = length // 2
        start = rng.randrange(half + 1)
        other = random_name(rng, half - 1, BINARY_ALPHABET) + "c"
        return [(base, True), (base[start : start + half], True), (other, False)]
    if mode == MODE_MEDIUM:
        return random_teams(rng, MEDIUM_NAMES, MEDIUM_LENGTH, SMALL_ALPHABET)
    if mode == MODE_PAIR:
        length = MAX_TOTAL // 2
        base = random_name(rng, length, SMALL_ALPHABET)
        other = random_name(rng, length - 1, SMALL_ALPHABET) + "z"
        return [(base, True), (other, bool(rng.randrange(2)))]
    if mode in (MODE_POSITIVE_RANDOM, MODE_POSITIVE_SHARED):
        values = rng.sample(range(len(ALPHABET) ** SHORT_LENGTH), POSITIVE_NAMES)
        core_length = POSITIVE_LENGTH - SHORT_LENGTH
        shared = (PERIOD * core_length)[:core_length]
        teams = []
        for value in values:
            if mode == MODE_POSITIVE_RANDOM:
                core = random_name(rng, core_length, BINARY_ALPHABET)
            else:
                core = shared
            teams.append((encoded_name(value) + core, True))
        return teams
    if mode == MODE_MAX_COUNT:
        names = [
            "".join(chars)
            for length in range(1, SHORT_LENGTH)
            for chars in itertools.product(ALPHABET, repeat=length)
        ]
        remaining = MAX_TOTAL - sum(map(len, names))
        count, remainder = divmod(remaining, SHORT_LENGTH)
        products = itertools.product(ALPHABET, repeat=SHORT_LENGTH)
        names.extend("".join(chars) for chars in itertools.islice(products, count))
        names[-1] += "a" * remainder
        return [(name, index == 0 or bool(rng.randrange(2))) for index, name in enumerate(names)]
    raise ValueError("unknown generator mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    teams = generate(mode, random.Random(seed))
    assert teams and teams[0][1]
    assert sum(len(name) for name, _ in teams) <= MAX_TOTAL
    assert len({name for name, _ in teams}) == len(teams)
    print(len(teams))
    for name, positive in teams:
        print(name + ("+" if positive else ""))


if __name__ == "__main__":
    main()
