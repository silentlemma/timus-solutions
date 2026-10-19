"""Validate any participant with the maximum literal number of comparisons."""

from pathlib import Path
import sys


def comparison_counts(values):
    counts = [0] * len(values)
    champion = 0
    for index in range(1, len(values)):
        counts[champion] += 1
        counts[index] += 1
        if values[index] < values[champion]:
            champion = index
    return counts


def check(values, output):
    tokens = output.split()
    if len(tokens) != 1:
        return False, "expected one integer identifier"
    try:
        identifier = int(tokens[0])
    except ValueError:
        return False, "identifier is not an integer"
    if not 1 <= identifier <= len(values):
        return False, "identifier outside the input range"
    counts = comparison_counts(values)
    if counts[identifier - 1] != max(counts):
        return False, "chosen participant does not attain the maximum comparison count"
    return True, "valid maximum-count participant"


if __name__ == "__main__":
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    assert data[0] == len(data) - 1
    accepted, reason = check(data[1:], Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
