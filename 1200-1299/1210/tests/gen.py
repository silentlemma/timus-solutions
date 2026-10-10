"""A map: a seed, the number of levels, the most planets per level, the
chance of a link in percent and a mode. In mode 1 every planet can be
reached; in mode 2 some planets have no way in but offer the richest
links onwards."""

import random
import sys

LOW, HIGH = -32768, 32767


def main():
    seed, levels, most, percent, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
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
