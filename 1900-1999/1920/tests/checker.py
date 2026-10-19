"""Validate any simple grid cycle; the expected path is not canonical."""

from pathlib import Path
import sys


def check(size, length, output):
    lines = output.strip().splitlines()
    if not lines:
        return False, "empty output"
    possible = length % 2 == 0 and length <= size * size
    if lines[0].strip() == "Unsuitable device":
        return (not possible and len(lines) == 1), "impossibility declaration"
    if lines[0].strip() != "Overwhelming power of magic":
        return False, "wrong heading"
    if not possible:
        return False, "cycle impossible by parity or vertex count"
    tokens = " ".join(lines[1:]).split()
    if len(tokens) != 2 * length:
        return False, "wrong coordinate count"
    try:
        values = list(map(int, tokens))
    except ValueError:
        return False, "noninteger coordinate"
    vertices = list(zip(values[::2], values[1::2]))
    if any(not (1 <= row <= size and 1 <= column <= size) for row, column in vertices):
        return False, "coordinate outside the grid"
    if len(set(vertices)) != length:
        return False, "repeated vertex"
    for first, second in zip(vertices, vertices[1:] + vertices[:1]):
        if abs(first[0] - second[0]) + abs(first[1] - second[1]) != 1:
            return False, "nonadjacent consecutive vertices or missing closing edge"
    return True, "valid simple cycle"


if __name__ == "__main__":
    grid_size, target_length = map(int, Path(sys.argv[1]).read_text().split())
    accepted, reason = check(grid_size, target_length, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
