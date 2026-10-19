from itertools import groupby
import sys


def safe_removals(values, budget):
    removed = 0
    spells = 0
    active = 0
    for threshold, cluster in groupby(sorted(values)):
        count = sum(1 for _ in cluster)
        if count * threshold > budget:
            break
        if (active + count) * threshold > budget:
            spells += 1
            active = 0
        active += count
        removed += count
    return removed, spells + (active > 0)


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count, budget = next(tokens), next(tokens)
    values = [next(tokens) for _ in range(count)]
    print(*safe_removals(values, budget))


if __name__ == "__main__":
    main()
