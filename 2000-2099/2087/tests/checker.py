"""Check the forced switch events, allowing any order of the output rows."""

from collections import Counter
from pathlib import Path
import sys

MAX_CHANGES = 200_000
MAX_DEPARTURE = 10**9
EVENT_FIELDS = 4
ARGUMENTS = 4


class Bad(Exception):
    pass


def events(path, height, width, switches):
    words = Path(path).read_text(encoding="utf-8").split()
    if not words:
        raise Bad("missing event count")
    try:
        count = int(words[0])
    except ValueError as error:
        raise Bad("event count is not an integer") from error
    if not 0 <= count <= MAX_CHANGES:
        raise Bad("event count is out of range")
    if len(words) != 1 + EVENT_FIELDS * count:
        raise Bad("event count does not match the number of fields")
    answer = Counter()
    for start in range(1, len(words), EVENT_FIELDS):
        try:
            time, row, column = map(int, words[start : start + EVENT_FIELDS - 1])
        except ValueError as error:
            raise Bad("an event field is not an integer") from error
        direction = words[start + EVENT_FIELDS - 1]
        if not 1 <= time <= MAX_DEPARTURE + height * width:
            raise Bad("event time is out of range")
        if not 1 <= row <= height or not 1 <= column <= width:
            raise Bad("event coordinates are out of range")
        if (row, column) not in switches:
            raise Bad("an event does not refer to a switch")
        if direction not in {"F", "L", "R"}:
            raise Bad("invalid switch direction")
        answer[time, row, column, direction] += 1
    return count, answer


def check(source, expected, output):
    lines = Path(source).read_text(encoding="utf-8").splitlines()
    height, width = map(int, lines[0].split())
    switches = {
        (row + 1, column + 1)
        for row in range(height)
        for column in range(width)
        if lines[1 + 2 * row][2 * column] in {"F", "L", "R"}
    }
    optimum, required = events(expected, height, width, switches)
    count, actual = events(output, height, width, switches)
    if count != optimum:
        raise Bad("the number of switch changes is not minimal")
    if actual != required:
        raise Bad("switch changes differ from the forced deadline events")


def main():
    try:
        if len(sys.argv) != ARGUMENTS:
            raise Bad("usage: python checker.py INPUT EXPECTED OUTPUT")
        check(*sys.argv[1:])
    except (Bad, OSError, ValueError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
