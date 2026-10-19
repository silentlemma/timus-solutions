"""Check any valid permutation; certify No by strict bridge-supply counts."""

from bisect import bisect_left, bisect_right
from collections import Counter
from pathlib import Path
import sys

MAXIMUM_COUNT = 100000
MAXIMUM_VOLUME = 1000000
ACTUAL_ARG = 3


def read_dolls(path):
    values = list(map(int, Path(path).read_text().split()))
    if not values:
        raise ValueError("empty input")
    n = values[0]
    if not 2 <= n <= MAXIMUM_COUNT or len(values) != 1 + 2 * n:
        raise ValueError("invalid input size")
    dolls = list(zip(values[1::2], values[2::2]))
    if any(not 1 <= a <= b <= MAXIMUM_VOLUME for a, b in dolls):
        raise ValueError("invalid volumes")
    return dolls


def has_order(dolls):
    points = Counter(a for a, b in dolls if a == b)
    starts = sorted(a for a, b in dolls if a < b)
    ends = sorted(b for a, b in dolls if a < b)
    for value, count in points.items():
        bridges = bisect_left(starts, value) - bisect_right(ends, value)
        if count > bridges + 1:
            return False
    return True


def check_answer(dolls, words):
    if not words:
        return False, "empty answer"
    if words[0] == "No":
        if len(words) != 1:
            return False, "extra tokens after No"
        return (False, "a valid order exists") if has_order(dolls) else (True, "valid No")
    if words[0] != "Yes":
        return False, "expected Yes or No"
    n = len(dolls)
    if len(words) != n + 1:
        return False, "wrong number of IDs"
    try:
        order = [int(value) - 1 for value in words[1:]]
    except ValueError:
        return False, "noninteger ID"
    seen = bytearray(n)
    for index in order:
        if not 0 <= index < n or seen[index]:
            return False, "ID outside range or repeated"
        seen[index] = 1
    for previous, following in zip(order, order[1:]):
        if dolls[previous][1] <= dolls[following][0]:
            return False, "an item fits into the next one"
    return True, "valid permutation"


def main():
    try:
        dolls = read_dolls(sys.argv[1])
        passed, detail = check_answer(dolls, Path(sys.argv[ACTUAL_ARG]).read_text().split())
    except (OSError, ValueError, IndexError) as error:
        passed, detail = False, str(error)
    print(detail)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
