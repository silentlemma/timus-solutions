"""A map: a seed, the number of levels, the most planets per level, the
chance of a link in percent and a mode.

Mode 1: every planet can be reached, with random widths and costs.
Mode 2: unreachable planets offer the richest links onwards.
Mode 3: every level has the maximum requested width, every link is
present, and every cost is -32768 (seed and percent are ignored).
Mode 4: widths alternate between the maximum requested width and one;
random links use zero, unit costs and both cost limits, with every planet
reachable. All randomness uses the supplied seed.
"""

import random
import sys

LOW, HIGH = -32768, 32767


def boundary_map(rng, levels, most, percent, mode):
    blocks, prev = [], 1
    for level in range(levels):
        count = most if mode == 3 or level % 2 == 0 else 1
        rows = [str(count)]
        for _ in range(count):
            if mode == 3:
                items = [(source, LOW) for source in range(1, prev + 1)]
            else:
                sources = [s for s in range(1, prev + 1) if rng.randrange(100) < percent]
                if not sources:
                    sources = [rng.randint(1, prev)]
                items = [(s, rng.choice([LOW, HIGH, 0, 0, 0, -1, 1])) for s in sources]
                rng.shuffle(items)
            rows.append(" ".join("%d %d" % pair for pair in items) + " 0")
        blocks.append("\n".join(rows))
        prev = count
    sys.stdout.write(str(levels) + "\n" + "\n*\n".join(blocks) + "\n")


def main():
    seed, levels, most, percent, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode in (3, 4):
        boundary_map(rng, levels, most, percent, mode)
        return
    blocks, prev, reach = [], 1, [True]
    for level in range(levels):
        k = rng.randint(1, most)
        rows, now = [str(k)], []
        for planet in range(k):
            cut = mode == 2 and planet > 0 and rng.random() < 0.3
            links = {}
            if not cut:
                open_ = [s for s in range(1, prev + 1) if reach[s - 1]]
                links[rng.choice(open_)] = rng.randint(LOW, HIGH)
                for src in range(1, prev + 1):
                    if rng.randrange(100) < percent:
                        links[src] = rng.randint(LOW, HIGH)
            for src in range(1, prev + 1):
                if not reach[src - 1]:
                    links[src] = LOW
            now.append(not cut and any(reach[s - 1] for s in links))
            items = list(links.items())
            rng.shuffle(items)
            rows.append(" ".join("%d %d" % p for p in items) + (" 0" if items else "0"))
        blocks.append("\n".join(rows))
        prev, reach = k, now
    sys.stdout.write(str(levels) + "\n" + "\n*\n".join(blocks) + "\n")


if __name__ == "__main__":
    main()
