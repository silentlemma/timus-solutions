"""Check an optimal queue by multiset equality and direct boarding simulation."""

from collections import Counter
from pathlib import Path
import sys


def check(input_text, expected_text, output_text):
    count, capacity, *values = map(int, input_text.split())
    try:
        result = list(map(int, output_text.split()))
    except ValueError:
        return "the output must contain integers"
    if len(result) != count + 1:
        return "expected the trip count and exactly n passenger values"
    claimed, order = result[0], result[1:]
    if Counter(order) != Counter(values):
        return "the queue is not a permutation of the input multiset"
    trips = 0
    pending = None
    for value in order:
        if pending is None:
            pending = value
        elif pending + value <= capacity:
            trips += 1
            pending = None
        else:
            trips += 1
            pending = value
    if pending is not None:
        trips += 1
    if claimed != trips:
        return "the reported count disagrees with boarding simulation"
    if claimed != int(expected_text.split()[0]):
        return "the queue does not attain the maximum trip count"
    return None


def main():
    input_path, expected_path, output_path = map(Path, sys.argv[1:])
    error = check(input_path.read_text(), expected_path.read_text(), output_path.read_text())
    if error is not None:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
