import random
import sys

MAX_CITIES = 100000
MAX_ROADS = 100000
PERCENT_SCALE = 100
DIAMOND_EDGES = 4


def generate(seed, mode):
    rng = random.Random(seed)
    count = MAX_CITIES
    start, target = 0, count - 1
    if mode in (1, 2):
        probability = 0 if mode == 1 else PERCENT_SCALE - 1
        edges = [(city, city + 1, probability) for city in range(count - 1)]
    elif mode == 3:
        edges = [(0, city, city % PERCENT_SCALE) for city in range(1, count)]
        edges.append((1, 2, 0))
    elif mode == 4:
        half = count // 2
        edges = [(city, city + 1, 0) for city in range(half - 1)]
        edges += [(half - 1, city, city % PERCENT_SCALE) for city in range(half, count)]
    elif mode == 5:
        edges = []
        tip = 0
        for _ in range(MAX_ROADS // DIAMOND_EDGES):
            first, second, following = tip + 1, tip + 2, tip + 3
            edges += [(tip, first, 1), (first, following, 0)]
            edges += [(tip, second, 0), (second, following, 0)]
            tip = following
        target = tip
    elif mode == 6:
        edges = [
            (rng.randrange(city), city, rng.randrange(PERCENT_SCALE))
            for city in range(1, count)
        ]
        seen = {tuple(sorted((first, second))) for first, second, _ in edges}
        while len(edges) < MAX_ROADS:
            first, second = sorted(rng.sample(range(count), 2))
            if (first, second) not in seen:
                edges.append((first, second, rng.randrange(PERCENT_SCALE)))
                seen.add((first, second))
        rng.shuffle(edges)
        start, target = count - 1, count // 2
    else:
        raise ValueError("unknown generator mode")
    return count, edges, start, target


def main():
    seed, mode = map(int, sys.argv[1:])
    count, edges, start, target = generate(seed, mode)
    lines = [f"{count} {len(edges)}", f"{start + 1} {target + 1}"]
    lines.extend(f"{first + 1} {second + 1} {probability}" for first, second, probability in edges)
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
