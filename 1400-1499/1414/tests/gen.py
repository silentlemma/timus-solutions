"""10 000 operations: a seed and a mode. Mode 1 uses short names over a
small alphabet so that queries match many names, mode 2 adds 9 000
distinct names of 20 characters and then asks 1 000 prefixes, mode 3
mixes letters and digits with many repeated additions."""

import random
import sys

OPS = 10000
LONG = 20


def name(rng, alphabet, low, high):
    return "".join(rng.choice(alphabet) for _ in range(rng.randint(low, high)))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    if mode == 1:
        for _ in range(OPS):
            op = "+" if rng.random() < 0.6 else "?"
            lines.append(op + name(rng, "abc", 1, 6 if op == "+" else 3))
    elif mode == 2:
        added = sorted(
            {name(rng, "abcdefghijklmnopqrstuvwxyz0123456789", LONG, LONG) for _ in range(9000)}
        )
        rng.shuffle(added)
        lines = ["+" + a for a in added]
        while len(lines) < OPS:
            lines.append("?" + rng.choice(added)[: rng.randint(1, 3)])
    else:
        pool = [name(rng, "sun0123456789", 1, 8) for _ in range(300)]
        for _ in range(OPS):
            if rng.random() < 0.7:
                lines.append("+" + rng.choice(pool))
            else:
                lines.append("?" + rng.choice(pool)[: rng.randint(1, 3)])
    print("\n".join(lines))


main()
