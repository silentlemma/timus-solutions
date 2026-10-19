"""Accept any two bounded nonnegative integer summands with the requested total."""

from pathlib import Path
import re
import sys


def validate(x, y, total, raw):
    low, high = max(0, total - y), min(x, total)
    try:
        words = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if words == ["Impossible"]:
        return low > high
    if len(words) != 2 or any(re.fullmatch(r"[+-]?[0-9]+", word) is None for word in words):
        return False
    try:
        a, b = map(int, words)
    except ValueError:
        return False
    return 0 <= a <= x and 0 <= b <= y and a + b == total


def main():
    x, y, total = map(int, Path(sys.argv[1]).read_text(encoding="ascii").split())
    if not validate(x, y, total, Path(sys.argv[3]).read_bytes()):
        print("Invalid bounded summands or false impossibility claim")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
