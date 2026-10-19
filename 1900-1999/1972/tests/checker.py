"""Verify an optimal simple path of one-option changes without trusting expected output."""
from pathlib import Path
import sys


def check(dimensions, start, finish, text):
    lines = text.splitlines()
    if not lines:
        return False
    try:
        size, = map(int, lines[0].split())
    except ValueError:
        return False
    optimal = (1 << dimensions) - int((start ^ finish).bit_count() % 2 == 0)
    if size != optimal or len(lines) != size + 1:
        return False
    seen = set()
    previous = None
    for line in lines[1:]:
        try:
            count, *enabled = map(int, line.split())
        except ValueError:
            return False
        if count != len(enabled) or enabled != sorted(set(enabled)):
            return False
        if any(not 1 <= bit <= dimensions for bit in enabled):
            return False
        mask = sum(1 << (bit - 1) for bit in enabled)
        if mask in seen or (previous is None and mask != start):
            return False
        if previous is not None:
            difference = previous ^ mask
            if difference == 0 or difference & (difference - 1):
                return False
        seen.add(mask)
        previous = mask
    return previous == finish


def main():
    tokens = iter(map(int, Path(sys.argv[1]).read_text().split()))
    dimensions = next(tokens)
    start = sum(1 << (next(tokens) - 1) for _ in range(next(tokens)))
    finish = sum(1 << (next(tokens) - 1) for _ in range(next(tokens)))
    if not check(dimensions, start, finish, Path(sys.argv[3]).read_text()):
        print('Expected a maximum simple one-option path between the given endpoints')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
