"""Accept any participant ordering with the latest possible strict certainty round."""

from pathlib import Path
import re
import sys

MAX_SCORE = 6


def read_case(text):
    data = list(map(int, text.split()))
    n = data[0]
    if not 2 <= n <= 1000 or len(data) != 2 * n + 1:
        raise ValueError("bad input size")
    if any(not 0 <= score <= MAX_SCORE for score in data[1:]):
        raise ValueError("bad score")
    return data[1 : n + 1], data[n + 1 :]


def optimum(first, second):
    n = len(first)
    if sum(first) == sum(second):
        return n
    leader, other = (first, second) if sum(first) > sum(second) else (second, first)
    low = [leader.count(value) for value in range(MAX_SCORE + 1)]
    high = [other.count(value) for value in range(MAX_SCORE + 1)]

    def extreme(counts, need, reverse):
        total = 0
        values = range(MAX_SCORE, -1, -1) if reverse else range(MAX_SCORE + 1)
        for value in values:
            take = min(need, counts[value])
            total += value * take
            need -= take
        return total

    for played in range(1, n):
        lead = extreme(low, played, False) - extreme(high, played, True)
        if lead > MAX_SCORE * (n - played):
            return played
    return n


def validate(text, first, second, optimal=None):
    n = len(first)
    tokens = text.split()
    if len(tokens) != 2 * n or any(re.fullmatch("[0-9]+", token) is None for token in tokens):
        return False
    ids = [int(token) - 1 for token in tokens]
    if set(ids[::2]) != set(range(n)) or set(ids[1::2]) != set(range(n)):
        return False
    difference = 0
    actual = n
    for played, (a, b) in enumerate(zip(ids[::2], ids[1::2]), 1):
        difference += first[a] - second[b]
        if abs(difference) > MAX_SCORE * (n - played):
            actual = played
            break
    return actual == (optimum(first, second) if optimal is None else optimal)


if __name__ == "__main__":
    try:
        data = read_case(Path(sys.argv[1]).read_text())
        passed = validate(Path(sys.argv[3]).read_text(), *data)
    except (OSError, ValueError, IndexError):
        passed = False
    if not passed:
        print("Expected two ID permutations maximizing the first strict winner-certainty round.")
    raise SystemExit(0 if passed else 1)
