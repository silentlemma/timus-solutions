import random
import sys

MAX_CITIES = 10000
MAX_ROADS = 100000
GROUP_SIZE = 100


def generate(seed, mode):
    rng = random.Random(seed)
    count = MAX_CITIES
    roads = []
    seen = set()

    def add(left, right, random_direction=False):
        pair = (min(left, right), max(left, right))
        if left == right or pair in seen:
            return
        seen.add(pair)
        if random_direction and rng.randrange(2):
            left, right = right, left
        roads.append((left, right))

    start, target = 0, count - 1
    if mode <= 3:
        for city in range(count - 1):
            reverse = mode != 3 and city % 2
            add(city + 1, city) if reverse else add(city, city + 1)
        if mode != 1:
            start, target = target, start
    elif mode == 5:
        groups = count // GROUP_SIZE
        for group in range(groups):
            anchor = group * GROUP_SIZE
            for offset in range(1, GROUP_SIZE):
                add(anchor, anchor + offset, True)
            if group + 1 < groups:
                following = anchor + GROUP_SIZE
                add(following, anchor) if group % 2 else add(anchor, following)
        while len(roads) < MAX_ROADS:
            anchor = rng.randrange(groups) * GROUP_SIZE
            left, right = rng.sample(range(anchor, anchor + GROUP_SIZE), 2)
            add(left, right, True)
        target = (groups - 1) * GROUP_SIZE
    elif mode == 7:
        add(0, 1)
        add(2, 1)
        target = 2
        while len(roads) < MAX_ROADS:
            left, right = rng.sample(range(3, count), 2)
            add(left, right, True)
    else:
        for city in range(count - 1):
            add(city, city + 1, mode == 4)
        while len(roads) < MAX_ROADS:
            left, right = sorted(rng.sample(range(count), 2))
            add(left, right, mode == 4)
        if mode == 6:
            start, target = target, start
    return count, roads, start, target


def main():
    seed, mode = map(int, sys.argv[1:])
    count, roads, start, target = generate(seed, mode)
    lines = [f"{count} {len(roads)}"]
    lines.extend(f"{left + 1} {right + 1}" for left, right in roads)
    lines.append(f"{start + 1} {target + 1}")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
