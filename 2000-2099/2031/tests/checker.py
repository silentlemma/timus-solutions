"""Check any two-digit row whose half-turn is a positive consecutive segment."""

from itertools import product
from pathlib import Path
import sys

ROTATION = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}


def feasible(count):
    targets = {int(ROTATION[b] + ROTATION[a]) for a, b in product(ROTATION, repeat=2)} - {0}
    return any(all(start + step in targets for step in range(count)) for start in targets)


def validate(count, raw):
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if tokens == ["Glupenky", "Pierre"]:
        return not feasible(count)
    if len(tokens) != count:
        return False
    if any(len(word) != 2 or any(ch not in ROTATION for ch in word) for word in tokens):
        return False
    values = [int(ROTATION[word[1]] + ROTATION[word[0]]) for word in reversed(tokens)]
    return values[0] > 0 and all(b == a + 1 for a, b in zip(values, values[1:]))


def main():
    count = int(Path(sys.argv[1]).read_text(encoding="ascii").strip())
    if not validate(count, Path(sys.argv[3]).read_bytes()):
        print("Invalid rotated sequence or false impossibility claim")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
