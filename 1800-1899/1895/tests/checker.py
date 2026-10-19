from collections import Counter
from pathlib import Path
import sys


def check(input_text, expected_text, output_text):
    window, capacity, n, *deadlines = map(int, input_text.split())
    optimum = int(expected_text.split()[0])
    try:
        values = list(map(int, output_text.split()))
    except ValueError:
        return "output must contain integers"
    if optimum == -1:
        return None if values == [-1] else "the instance is impossible"
    if len(values) != 1 + 2 * n:
        return "expected an optimum and two times per order"
    if values[0] != optimum:
        return "the number of active minutes is not optimal"
    used = Counter()
    starts = iter(values[1:])
    for deadline, first, second in zip(deadlines, starts, starts):
        if not max(0, deadline - window) <= first < second < deadline:
            return "a side violates its release, deadline or order"
        used[first] += 1
        used[second] += 1
    if max(used.values()) > capacity:
        return "the pan capacity is exceeded"
    if len(used) != values[0]:
        return "the reported number of active minutes is incorrect"
    return None


def main():
    input_path, expected_path, output_path = map(Path, sys.argv[1:])
    error = check(
        input_path.read_text(), expected_path.read_text(), output_path.read_text()
    )
    if error is not None:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
