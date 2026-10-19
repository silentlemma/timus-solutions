"""Validate any winning permutation using exact play and constant-space cycle detection."""

from collections import deque
from itertools import permutations
from pathlib import Path
import re
import sys

LOCAL_LIMIT = 5
INTEGER = re.compile(r"[+-]?[0-9]+\Z")


def game_won(first, second):
    first, second = deque(first), deque(second)
    saved_first, saved_second = first.copy(), second.copy()
    power, steps = 1, 0
    while first and second:
        x, y = first.popleft(), second.popleft()
        if x > y:
            first.extend((y, x))
        elif y > x:
            second.extend((x, y))
        if not first or not second:
            break
        steps += 1
        if first == saved_first and second == saved_second:
            return False
        if steps == power:
            saved_first, saved_second = first.copy(), second.copy()
            power *= 2
            steps = 0
    return bool(first)


def check(input_path, actual_path):
    data = list(map(int, Path(input_path).read_text(encoding="utf-8").split()))
    size, opponent = data[0], data[1:]
    if len(opponent) != size or sorted(opponent) != list(range(1, size + 1)):
        raise ValueError("invalid input permutation")
    words = Path(actual_path).read_text(encoding="utf-8").split()
    if words == ["NO"]:
        if size >= LOCAL_LIMIT:
            return False, "a winning five-card embedding exists"
        possible = any(
            game_won(own, opponent) for own in permutations(range(1, size + 1))
        )
        return not possible, "NO audited by exhaustive play"
    if len(words) != size + 1 or words[0] != "YES":
        return False, "wrong output shape"
    if not all(INTEGER.fullmatch(word) for word in words[1:]):
        return False, "card must be an integer"
    own = list(map(int, words[1:]))
    if sorted(own) != list(range(1, size + 1)):
        return False, "not a permutation"
    valid = game_won(own, opponent)
    return valid, "OK" if valid else "deck does not win"


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("usage: checker.py INPUT EXPECTED ACTUAL")
        accepted, reason = check(sys.argv[1], sys.argv[3])
    except (OSError, ValueError, IndexError):
        accepted, reason = False, "invalid input or output"
    print(reason)
    sys.exit(0 if accepted else 1)
