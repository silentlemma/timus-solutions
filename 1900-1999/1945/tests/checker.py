"""Check any hall assignment by literal possible parents, without modular valuation assumptions."""

from pathlib import Path
import re
import sys

MIN_GROUPS = 2
MAX_GROUPS = 5
MAX_VISITORS = 50000
MAX_ARMS = 1000000000
INTEGER = re.compile(r"[+-]?[0-9]+\Z")


def valid_assignment(values, groups, colors):
    masks = {}
    for value, color in zip(values, colors):
        bit = 1 << (color - 1)
        for ordinal in range(1, groups + 1):
            if value % ordinal == 0:
                parent = value // ordinal
                previous = masks.get(parent, 0)
                if previous & bit:
                    return False
                masks[parent] = previous | bit
    return True


def check(input_path, actual_path):
    data = list(map(int, Path(input_path).read_text(encoding="utf-8").split()))
    size, groups = data[:2]
    values = data[2:]
    if not (1 <= size <= MAX_VISITORS and MIN_GROUPS <= groups <= MAX_GROUPS):
        raise ValueError("invalid input limits")
    if len(values) != size or len(set(values)) != size:
        raise ValueError("invalid input values")
    if any(not 1 <= value <= MAX_ARMS for value in values):
        raise ValueError("invalid arm count")
    words = Path(actual_path).read_text(encoding="utf-8").split()
    if words == ["No"]:
        return False, "a valuation coloring always exists for g=2..5"
    if len(words) != size + 1 or words[0] != "Yes":
        return False, "wrong output shape"
    if not all(INTEGER.fullmatch(word) for word in words[1:]):
        return False, "hall must be an integer"
    colors = list(map(int, words[1:]))
    if any(not 1 <= color <= groups for color in colors):
        return False, "hall outside 1..g"
    valid = valid_assignment(values, groups, colors)
    return valid, "OK" if valid else "possible brothers share a hall"


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("usage: checker.py INPUT EXPECTED ACTUAL")
        accepted, reason = check(sys.argv[1], sys.argv[3])
    except (OSError, ValueError, IndexError):
        accepted, reason = False, "invalid input or output"
    print(reason)
    sys.exit(0 if accepted else 1)
