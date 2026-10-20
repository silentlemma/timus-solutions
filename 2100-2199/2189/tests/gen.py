"""Generate deterministic point updates: python gen.py MODE SEED."""

import random
import sys

MAX_SIZE = 100_000
MAX_ROLE = 1_000_000_000
SMALL_SIZE = 12
SMALL_QUERIES = 40
SMALL_ROLES = 5
GROUP_SIZE = 317
HOT_COUNT = 10
FRESH_OFFSET = MAX_SIZE + 1
DENSE = 3
NO_OP = 4
MERGE = 5
SEPARATE = 6
HOT = 7
SINGLE = 8
GROUPS = 9
FRESH = 10
MEDIUM = 11
WORD_BITS = 64
MEDIUM_SIZE = 2_000
MEDIUM_MIN_QUERIES = 200
MEDIUM_ROLES = 100


def generate(mode, rng):
    if mode == 1:
        n = rng.randint(1, SMALL_SIZE)
        q = rng.randint(1, SMALL_QUERIES)
        roles = rng.sample(range(1, MAX_ROLE + 1), SMALL_ROLES)
        initial = [rng.choice(roles) for _ in range(n)]
        current = initial[:]
        updates = []
        for _ in range(q):
            index = rng.randrange(n)
            kind = rng.randrange(SMALL_ROLES)
            if kind == 0:
                role = current[index]
            elif kind == 1:
                role = rng.randint(1, MAX_ROLE)
            else:
                role = rng.choice(roles)
            updates.append((index + 1, role))
            current[index] = role
    elif mode == 2:
        n = q = MAX_SIZE
        initial = rng.sample(range(1, MAX_ROLE + 1), n)
        current = initial[:]
        updates = []
        for _ in range(q):
            index = rng.randrange(n)
            role = rng.choice(current) if rng.randrange(2) else rng.randint(1, MAX_ROLE)
            updates.append((index + 1, role))
            current[index] = role
    elif mode == DENSE:
        n = q = MAX_SIZE
        initial = [rng.randint(1, 2) for _ in range(n)]
        updates = [(rng.randint(1, n), rng.randint(1, 2)) for _ in range(q)]
    elif mode == NO_OP:
        n = q = MAX_SIZE
        initial = list(range(1, n + 1))
        updates = [(index, index) for index in rng.choices(range(1, n + 1), k=q)]
    elif mode == MERGE:
        n = q = MAX_SIZE
        initial = list(range(1, n + 1))
        order = list(range(1, n + 1))
        rng.shuffle(order)
        updates = [(index, 1) for index in order]
    elif mode == SEPARATE:
        n = q = MAX_SIZE
        initial = [MAX_ROLE] * n
        order = list(range(1, n + 1))
        rng.shuffle(order)
        updates = [(index, index) for index in order]
    elif mode == HOT:
        n = q = MAX_SIZE
        initial = [1 + index % 2 for index in range(n)]
        positions = [1, n, n // 2, n // 2 + 1]
        positions += rng.sample(range(1, n + 1), HOT_COUNT)
        roles = [1, 2, MAX_ROLE]
        updates = [(rng.choice(positions), rng.choice(roles)) for _ in range(q)]
    elif mode == SINGLE:
        n, q = 1, MAX_SIZE
        initial = [MAX_ROLE]
        roles = [1, MAX_ROLE, rng.randint(1, MAX_ROLE)]
        updates = [(1, rng.choice(roles)) for _ in range(q)]
    elif mode == GROUPS:
        n = q = MAX_SIZE
        initial = [1 + index // GROUP_SIZE for index in range(n)]
        last_role = initial[-1]
        updates = [(rng.randint(1, n), rng.randint(1, last_role)) for _ in range(q)]
    elif mode == FRESH:
        n = q = MAX_SIZE
        initial = list(range(1, n + 1))
        order = list(range(1, n + 1))
        rng.shuffle(order)
        updates = [(index, FRESH_OFFSET + day) for day, index in enumerate(order)]
    elif mode == MEDIUM:
        boundaries = [WORD_BITS, WORD_BITS + 1, 2 * WORD_BITS - 1, 2 * WORD_BITS]
        n = rng.choice(boundaries + [rng.randint(WORD_BITS, MEDIUM_SIZE)])
        q = rng.randint(MEDIUM_MIN_QUERIES, MEDIUM_SIZE)
        roles = list(range(1, rng.randint(1, MEDIUM_ROLES) + 1))
        initial = [1] * n if rng.randrange(2) else [rng.choice(roles) for _ in range(n)]
        current = initial[:]
        updates = []
        for _ in range(q):
            index = rng.randrange(n)
            kind = rng.randrange(SMALL_ROLES)
            if kind == 0:
                role = current[index]
            elif kind == 1:
                role = rng.randint(1, MAX_ROLE)
            else:
                role = rng.choice(roles)
            updates.append((index + 1, role))
            current[index] = role
    else:
        raise SystemExit("unknown mode")
    return n, q, initial, updates


def main():
    mode, seed = map(int, sys.argv[1:])
    n, q, initial, updates = generate(mode, random.Random(seed))
    output = [f"{n} {q}", " ".join(map(str, initial))]
    output.extend(f"{index} {role}" for index, role in updates)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
