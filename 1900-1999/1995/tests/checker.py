"""Check minimum total and any valid positive-weight sequence, including unsorted ones."""

from pathlib import Path
import sys

PERCENT_SCALE = 100


def judge(size, wanted_kept, percentage, optimum, output):
    try:
        values = list(map(int, output.split()))
    except ValueError:
        return False, "noninteger output"
    if len(values) != size + 1:
        return False, "wrong number of output integers"
    declared, weights = values[0], values[1:]
    if any(value <= 0 for value in weights):
        return False, "weights must be positive"
    if declared != sum(weights) or declared != optimum:
        return False, "wrong sum or nonoptimal total"
    coordinates = sorted(set(weights))
    ranks = {value: i for i, value in enumerate(coordinates)}
    tree = [0] * (len(coordinates) + 1)
    kept = 0
    for position, value in enumerate(weights):
        # Zero-based rank counts only strictly smaller previous values.
        index, lighter = ranks[value], 0
        while index:
            lighter += tree[index]
            index -= index & -index
        if position and PERCENT_SCALE * lighter >= percentage * position:
            kept += 1
        index = ranks[value] + 1
        while index < len(tree):
            tree[index] += 1
            index += index & -index
    return (True, "ok") if kept == wanted_kept else (False, "wrong number of kept packages")


def main():
    size, kept, percentage = map(int, Path(sys.argv[1]).read_text().split())
    expected = Path(sys.argv[2]).read_text().split()
    optimum = int(expected[0])
    passed, detail = judge(size, kept, percentage, optimum, Path(sys.argv[3]).read_text())
    print(detail)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
