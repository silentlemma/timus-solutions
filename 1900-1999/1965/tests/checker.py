"""Check input, expected, candidate: both nonempty monotone subsequences or verified Fail."""
from pathlib import Path
import sys


def check(values, expected, candidate):
    size = len(values)
    if candidate.split() == ['Fail']:
        return expected.split() == ['Fail']
    lines = candidate.splitlines()
    if len(lines) != 3:
        return False
    try:
        counts = list(map(int, lines[0].split()))
        groups = [list(map(int, line.split())) for line in lines[1:]]
    except ValueError:
        return False
    if len(counts) != 2 or sum(counts) != size or any(c < 1 or c >= size for c in counts):
        return False
    if counts != list(map(len, groups)):
        return False
    positions = [0] * (size + 1)
    for i, value in enumerate(values):
        positions[value] = i
    seen = [False] * (size + 1)
    for group in groups:
        previous_position = -1
        increasing = decreasing = True
        previous_value = None
        for value in group:
            if value < 1 or value > size or seen[value]:
                return False
            if positions[value] <= previous_position:
                return False
            seen[value] = True
            previous_position = positions[value]
            if previous_value is not None:
                increasing &= previous_value < value
                decreasing &= previous_value > value
            previous_value = value
        if not increasing and not decreasing:
            return False
    return True


def main():
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    size, values = data[0], data[1:]
    if len(values) != size or sorted(values) != list(range(1, size + 1)):
        print('Invalid input permutation')
        return 1
    expected = Path(sys.argv[2]).read_text()
    candidate = Path(sys.argv[3]).read_text()
    if not check(values, expected, candidate):
        print('Expected two nonempty monotone input subsequences, or the verified Fail marker')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
