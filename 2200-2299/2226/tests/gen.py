"""Generate a tree with distinct edge lengths: python gen.py MODE SEED."""

import random
import sys

MAX_N = 10**5
MAX_LENGTH = 10**9
SMALL_N = 20
MEDIUM_N = 2000
MODES = (
    "small",
    "medium",
    "random",
    "path-up",
    "path-down",
    "path-zigzag",
    "star",
    "balanced",
    "broom",
    "caterpillar",
    "double-star",
)


def generate(mode, seed):
    if mode not in MODES:
        raise ValueError("unknown mode: " + mode)
    rng = random.Random(seed)
    n = MAX_N
    if mode == "small":
        n = rng.randint(2, SMALL_N)
    elif mode == "medium":
        n = rng.randint(SMALL_N + 1, MEDIUM_N)

    spine = n // 2
    edges = []
    for v in range(2, n + 1):
        if mode.startswith("path-"):
            u = v - 1
        elif mode == "star":
            u = 1
        elif mode == "balanced":
            u = v // 2
        elif mode == "broom":
            u = v - 1 if v <= spine else spine
        elif mode == "caterpillar":
            u = v - 1 if v <= spine else rng.randint(1, spine)
        elif mode == "double-star":
            u = 1 if v == 2 else rng.randint(1, 2)
        else:
            u = rng.randrange(1, v)
        edges.append((u, v))

    if n == 2:
        lengths = [rng.choice((1, MAX_LENGTH))]
    else:
        lengths = rng.sample(range(2, MAX_LENGTH), n - 1 - 2)
        lengths.extend((1, MAX_LENGTH))
    if mode == "path-up":
        lengths.sort()
    elif mode == "path-down":
        lengths.sort(reverse=True)
    elif mode == "path-zigzag":
        ordered = sorted(lengths)
        lengths = []
        left, right = 0, len(ordered) - 1
        while left <= right:
            lengths.append(ordered[left])
            left += 1
            if left <= right:
                lengths.append(ordered[right])
                right -= 1
    else:
        rng.shuffle(lengths)

    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    lines = []
    for (u, v), length in zip(edges, lengths):
        u, v = labels[u - 1], labels[v - 1]
        if rng.randrange(2):
            u, v = v, u
        lines.append(f"{u} {v} {length}\n")
    rng.shuffle(lines)
    return f"{n}\n" + "".join(lines)


def main():
    if len(sys.argv) != 1 + 2:
        raise SystemExit("usage: python gen.py MODE SEED")
    sys.stdout.write(generate(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
