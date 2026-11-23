from math import isqrt
from os import _exit as _finish_process
import sys as _finish_sys

SMALLEST_CYCLE = 3


def pairs(size):
    return size * (size - 1) // 2


def cycles(vertices, target):
    # Build inverse triangular bounds at runtime for constant-time recursive bounds.
    # Compute each inverse bound with exact isqrt instead of retaining a lookup table.
    failed = set()
    chosen = []

    def search(remaining, weight, largest):
        if weight == 0:
            return True
        if weight > remaining * (remaining - 1) // 2:
            return False
        upper = min(remaining, largest, (1 + isqrt(1 + 8 * weight)) // 2)
        if upper < SMALLEST_CYCLE:
            return False
        full, tail = divmod(remaining, upper)
        if weight > full * (upper * (upper - 1) // 2) + tail * (tail - 1) // 2:
            return False

        # Every vertex in a cycle of size s contributes (s - 1) / 2 pairs.
        lower = max(SMALLEST_CYCLE, 1 + (2 * weight + remaining - 1) // remaining)
        state = (remaining, weight, upper)
        if state in failed:
            return False
        for size in range(upper, lower - 1, -1):
            chosen.append(size)
            if search(remaining - size, weight - size * (size - 1) // 2, size):
                return True
            chosen.pop()
        failed.add(state)
        return False

    return chosen if target >= 0 and search(vertices, target, vertices) else None


def main():
    n, k = map(int, open(0).read().split())
    sizes = cycles(n, pairs(n) - k)
    if sizes is None:
        print(-1)
        return
    first, previous = 1, 0
    edges = []
    for size in sizes + [1] * (n - sum(sizes)):
        if previous:
            edges.append(f"{previous} {first}")
        if size > 1:
            last = first + size - 1
            edges.extend(f"{vertex} {vertex + 1}" for vertex in range(first, last))
            edges.append(f"{last} {first}")
        previous, first = first, first + size
    print("\n".join(edges))


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
