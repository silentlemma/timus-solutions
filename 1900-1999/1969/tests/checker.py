"""Check input, expected, candidate by endpoint motion and exact observed passage times."""
from pathlib import Path
import sys


SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
TIME_PARTS = 3
TIME_WIDTH = 8


def parse_time(text):
    parts = text.split(':')
    if len(text) != TIME_WIDTH or len(parts) != TIME_PARTS or any(len(p) != 2 for p in parts):
        raise ValueError('Expected HH:MM:SS')
    if any(not p.isascii() or not p.isdigit() for p in parts):
        raise ValueError('Expected decimal time digits')
    hours, minutes, seconds = map(int, parts)
    if not (0 <= hours < HOURS_PER_DAY and 0 <= minutes < MINUTES_PER_HOUR
            and 0 <= seconds < SECONDS_PER_MINUTE):
        raise ValueError('Time outside day')
    return (hours * MINUTES_PER_HOUR + minutes) * SECONDS_PER_MINUTE + seconds


def check(first, passages, candidate):
    lines = candidate.splitlines()
    if not lines:
        return False
    try:
        visits = [[parse_time(word) for word in line.split()] for line in lines]
    except ValueError:
        return False
    size = len(visits[0])
    if size < TIME_PARTS or size % 2 != 1 or len(visits) * (size - 1) != len(passages):
        return False
    if any(len(row) != size for row in visits):
        return False
    if visits[0][0] != first:
        return False
    duration = visits[0][1] - first
    offset = passages[0] - first
    if not 0 < offset < duration:
        return False
    starts = [row[0] for row in visits]
    if starts != sorted(set(starts)) or starts[-1] >= first + 2 * duration:
        return False
    observed = []
    for row in visits:
        if any(b - a != duration for a, b in zip(row, row[1:])):
            return False
        for leg, start in enumerate(row[:-1]):
            observed.append(start + (offset if leg % 2 == 0 else duration - offset))
    return len(set(observed)) == len(observed) and sorted(observed) == list(passages)


def main():
    words = Path(sys.argv[1]).read_text().split()
    times = [parse_time(word) for word in words]
    if not check(times[0], times[1:], Path(sys.argv[3]).read_text()):
        print('Expected equal-round-trip schedules with the exact observed passages')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
