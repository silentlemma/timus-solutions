import sys


def build(limit, maximum_spies):
    choose = [[1.0]]
    for size in range(1, limit + 1):
        previous = choose[-1]
        choose.append([1.0] + [previous[j - 1] + previous[j] for j in range(1, size)] + [1.0])
    table = [[0.0] * (maximum_spies + 1) for _ in range(limit + 1)]
    for size in range(1, limit + 1):
        table[size][0] = float(size)
        denominators = choose[size]
        for spies in range(1, min(maximum_spies, size - 1) + 1):
            loyal = size - spies
            loyal_counts, spy_counts = choose[loyal], choose[spies]
            best = 0.0
            for retained in range(1, size):
                lower = max(0, retained - loyal)
                upper = min(spies, (retained - 1) // 2)
                weighted = 0.0
                for remaining in range(lower, upper + 1):
                    weighted += (
                        spy_counts[remaining]
                        * loyal_counts[retained - remaining]
                        * table[retained - remaining][remaining]
                    )
                expected = weighted / denominators[retained]
                if expected > best:
                    best = expected
            table[size][spies] = best
    return table


def solve(total, spies):
    if total <= 2 * spies:
        return 0.0
    return build(total - spies, spies)[total - spies][spies]


def main():
    total, spies = map(int, sys.stdin.buffer.read().split())
    print(f"{solve(total, spies):.12f}")


if __name__ == "__main__":
    main()
