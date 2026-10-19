"""Check binary alphabet, optimal length and every order-n binary window."""

from pathlib import Path
import sys

MIN_ORDER = 1
MAX_ORDER = 20
ZERO = ord("0")
ONE = ord("1")


def check(order, data):
    words = data.split()
    if len(words) != 1:
        return False
    answer = words[0]
    size = 1 << order
    if len(answer) != size + order - 1:
        return False
    covered = bytearray(size)
    mask = size - 1
    window = 0
    for at, character in enumerate(answer):
        if character not in (ZERO, ONE):
            return False
        window = ((window << 1) | (character - ZERO)) & mask
        if at >= order - 1:
            covered[window] = 1
    return all(covered)


if __name__ == "__main__":
    input_path, _, output_path = map(Path, sys.argv[1:])
    order = int(input_path.read_text())
    if not MIN_ORDER <= order <= MAX_ORDER:
        raise ValueError("invalid input order")
    valid = check(order, output_path.read_bytes())
    print("OK" if valid else "invalid binary coverage or nonminimum length")
    sys.exit(0 if valid else 1)
