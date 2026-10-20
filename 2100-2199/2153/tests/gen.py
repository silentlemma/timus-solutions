import random
import sys


ROLES = "WMCR"
ROLE_COUNT = len(ROLES)
MAX_MEMBERS = 15
FULL_MASK = (1 << ROLE_COUNT) - 1
MODES = {
    "random",
    "maximum",
    "dense",
    "bottleneck",
    "singletons",
    "repeated",
    "chain",
    "masks",
}


def subset(rng, pool):
    choices = [mask for mask in range(1, FULL_MASK + 1) if mask & pool == mask]
    return rng.choice(choices)


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "random":
        count = rng.randint(1, MAX_MEMBERS)
        return [rng.randint(1, FULL_MASK) for _ in range(count)]
    if mode == "maximum":
        return [rng.randint(1, FULL_MASK) for _ in range(MAX_MEMBERS)]
    if mode == "dense":
        choices = [mask for mask in range(1, FULL_MASK + 1) if mask.bit_count() >= ROLE_COUNT - 1]
        return [rng.choice(choices) for _ in range(MAX_MEMBERS)]
    if mode == "bottleneck":
        choices = [mask for mask in range(1, FULL_MASK) if mask.bit_count() <= ROLE_COUNT - 2]
        pool = rng.choice(choices)
        people = [subset(rng, pool) for _ in range(MAX_MEMBERS - 1)]
        people.append(FULL_MASK)
        rng.shuffle(people)
        return people
    if mode == "singletons":
        count = rng.randint(1, MAX_MEMBERS)
        return [1 << rng.randrange(ROLE_COUNT) for _ in range(count)]
    if mode == "repeated":
        return [rng.randint(1, FULL_MASK)] * MAX_MEMBERS
    if mode == "chain":
        roles = rng.sample(range(ROLE_COUNT), ROLE_COUNT)
        people = [(1 << first) | (1 << second) for first, second in zip(roles, roles[1:])]
        count = rng.randint(ROLE_COUNT, MAX_MEMBERS)
        people.extend([1 << roles[0]] * (count - len(people)))
        return people
    people = list(range(1, FULL_MASK + 1))
    rng.shuffle(people)
    return people


def main():
    if len(sys.argv) != 1 + 2 or sys.argv[1] not in MODES:
        raise SystemExit("usage: python gen.py MODE SEED")
    people = generate(sys.argv[1], int(sys.argv[2]))
    print(len(people))
    for mask in people:
        print("".join(role for index, role in enumerate(ROLES) if mask & (1 << index)))


if __name__ == "__main__":
    main()
