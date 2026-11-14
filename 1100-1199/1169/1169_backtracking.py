from math import isqrt

SMALLEST_CYCLE = 3
TRIANGULAR_DISCRIMINANT_FACTOR = 8


def pairs(size):
    return size * (size - 1) // 2


def cycles(vertices, target):
    failed = set()
    chosen = []

    def search(remaining, weight, largest):
        if weight == 0:
            return True
        if weight > pairs(remaining):
            return False
        discriminant = 1 + TRIANGULAR_DISCRIMINANT_FACTOR * weight
        upper = min(remaining, largest, (1 + isqrt(discriminant)) // 2)
        # Every vertex in a cycle of size s contributes (s - 1) / 2 pairs.
        lower = max(SMALLEST_CYCLE, 1 + (2 * weight + remaining - 1) // remaining)
        state = (remaining, weight, upper)
        if state in failed:
            return False
        for size in range(upper, lower - 1, -1):
            chosen.append(size)
            if search(remaining - size, weight - pairs(size), size):
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
