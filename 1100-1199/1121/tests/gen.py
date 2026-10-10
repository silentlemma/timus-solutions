"""Random city maps: a seed, H, W, the share of crossings with branches in
per mille and the number of branch types (bits) to draw from."""

import random
import sys

MILLE = 1000


def main():
    seed, h, w, share, types = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    rows = []
    for _ in range(h):
        row = []
        for _ in range(w):
            mask = 0
            if rng.randrange(MILLE) < share:
                while not mask:
                    mask = rng.getrandbits(types)
            row.append(mask)
        rows.append(" ".join(map(str, row)))
    sys.stdout.write("%d %d\n" % (h, w) + "\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
