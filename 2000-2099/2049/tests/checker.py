"""Simulate any claimed transfer sequence; never require a particular construction."""

from pathlib import Path
import re
import sys

MAX_TUBES = 100000
MOVE_FACTOR = 3


def feasible(n, k):
    return k & (k - 1) == 0 or n >= k + 1 + (k & 1)


def validate(n, k, raw):
    if not 1 <= k <= n <= MAX_TUBES:
        return False
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if tokens == ["-1"]:
        return not feasible(n, k)
    if not tokens or any(re.fullmatch(r"[0-9]+", word) is None for word in tokens):
        return False
    try:
        values = list(map(int, tokens))
    except ValueError:
        return False
    count = values[0]
    if count > MOVE_FACTOR * n or len(values) != 1 + 2 * count:
        return False
    volumes = [1] * n
    for position in range(1, len(values), 2):
        donor, receiver = values[position] - 1, values[position + 1] - 1
        if not 0 <= donor < n or not 0 <= receiver < n or donor == receiver:
            return False
        amount = volumes[receiver]
        if volumes[donor] < amount:
            return False
        volumes[donor] -= amount
        volumes[receiver] += amount
    return volumes[0] == k and sum(volumes) == n and min(volumes) >= 0


def main():
    n, k = map(int, Path(sys.argv[1]).read_text(encoding="ascii").split())
    if not validate(n, k, Path(sys.argv[3]).read_bytes()):
        print("Incorrect move count, index, transfer, target volume or impossibility claim")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
