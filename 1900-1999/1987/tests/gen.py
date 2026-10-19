"""Usage: gen.py SEED MODE; modes: chain, same_start, same_end, disjoint, forest, late, repeat, near_limit, small."""

import random
import sys

MAXIMUM = 100000
LIMIT = 1000000000
GROUP_SIZE = 5
GROUP_SPAN = 10
DISJOINT_SPAN = 3

MODES = ("chain", "same_start", "same_end", "disjoint", "forest", "late", "repeat", "near_limit")


def generate(seed, mode):
    n = m = MAXIMUM
    if mode == "small":
        rng = random.Random(seed)
        wanted = rng.randint(1, 25)
        segments = []
        for _ in range(1500):
            a, b = sorted(rng.sample(range(1, 61), 2))
            if (a, b) not in segments and all(
                b < c or d < a or a <= c <= d <= b or c <= a <= b <= d for c, d in segments
            ):
                segments.append((a, b))
            if len(segments) == wanted:
                break
        segments.sort(key=lambda p: (p[0], -p[1]))
        points = [1, LIMIT] + [rng.randint(1, 65) for _ in range(40)]
        points.extend(v for pair in segments for v in pair)
        return segments, sorted(points)
    assert mode in MODES
    if mode == "same_start":
        segments = [(1, 2 * n + 1 - i) for i in range(n)]
    elif mode == "same_end":
        segments = [(i + 1, 2 * n + 1) for i in range(n)]
    elif mode in ("disjoint", "near_limit"):
        shift = LIMIT - DISJOINT_SPAN * n if mode == "near_limit" else 0
        segments = [
            (shift + DISJOINT_SPAN * i + 2, shift + DISJOINT_SPAN * i + DISJOINT_SPAN)
            for i in range(n)
        ]
    elif mode == "forest":
        segments = []
        for group in range(n // GROUP_SIZE):
            a = 1 + GROUP_SPAN * group
            segments.extend(((a, a + 8), (a, a + 2), (a, a + 1), (a + 4, a + 7), (a + 5, a + 6)))
    else:
        segments = [(i + 1, 2 * n + 1 - i) for i in range(n)]
    if mode == "late":
        points = [LIMIT] * m
    elif mode == "repeat":
        points = [n + 1] * m
    elif mode == "near_limit":
        points = [LIMIT - DISJOINT_SPAN * n + i * (DISJOINT_SPAN * n) // (m - 1) for i in range(m)]
        points[0] = 1
    else:
        span = (
            DISJOINT_SPAN * n + 2
            if mode == "disjoint"
            else GROUP_SPAN * (n // GROUP_SIZE) + 2
            if mode == "forest"
            else 2 * n + 2
        )
        points = [1 + i * span // (m - 1) for i in range(m)]
        points[-1] = LIMIT
    return segments, points


def render(segments, queries):
    return (
        str(len(segments))
        + "\n"
        + "".join(f"{a} {b}\n" for a, b in segments)
        + str(len(queries))
        + "\n"
        + "".join(f"{q}\n" for q in queries)
    )


if __name__ == "__main__":
    segments, queries = generate(int(sys.argv[1]), sys.argv[2])
    sys.stdout.write(render(segments, queries))
