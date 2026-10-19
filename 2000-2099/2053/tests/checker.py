"""Accept any valid sixteen-point planar straight-line graph with enough simple cycles."""

from array import array
from pathlib import Path
import re
import sys

VERTICES = 16
COORDINATE_BOUND = 1000
CYCLE_LIMIT = 300000
MIN_CYCLE_LENGTH = 3


def parse_graph(raw, size=VERTICES):
    try:
        lines = [line.strip() for line in raw.decode("ascii").splitlines() if line.strip()]
        if len(lines) != 2 * size:
            return None
        points = []
        for line in lines[:size]:
            words = line.split()
            if len(words) != 2 or any(re.fullmatch(r"[+-]?[0-9]+", word) is None for word in words):
                return None
            points.append(tuple(map(int, words)))
        adjacency = []
        for line in lines[size:]:
            bits = "".join(line.split())
            if len(bits) != size or any(bit not in "01" for bit in bits):
                return None
            adjacency.append(sum(1 << j for j, bit in enumerate(bits) if bit == "1"))
        for vertex in range(size):
            if adjacency[vertex] & (1 << vertex):
                return None
            for other in range(size):
                if bool(adjacency[vertex] & (1 << other)) != bool(adjacency[other] & (1 << vertex)):
                    return None
        return points, adjacency
    except (UnicodeDecodeError, ValueError):
        return None


def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a, b, p):
    return (
        orientation(a, b, p) == 0
        and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def geometric(points, adjacency):
    size = len(points)
    if len(set(points)) != size or any(abs(x) > COORDINATE_BOUND for p in points for x in p):
        return False
    edges = [(a, b) for a in range(size) for b in range(a + 1, size) if adjacency[a] & (1 << b)]
    for a, b in edges:
        if any(
            v not in (a, b) and on_segment(points[a], points[b], p) for v, p in enumerate(points)
        ):
            return False
    for index, (a, b) in enumerate(edges):
        for c, d in edges[index + 1 :]:
            if len({a, b, c, d}) < 4:
                continue
            pa, pb, pc, pd = points[a], points[b], points[c], points[d]
            x, y = orientation(pa, pb, pc), orientation(pa, pb, pd)
            z, w = orientation(pc, pd, pa), orientation(pc, pd, pb)
            if x * y < 0 and z * w < 0:
                return False
            if on_segment(pa, pb, pc) or on_segment(pa, pb, pd):
                return False
            if on_segment(pc, pd, pa) or on_segment(pc, pd, pb):
                return False
    return True


def cycle_histogram(adjacency):
    size = len(adjacency)
    full = (1 << size) - 1
    paths = array("Q", [0]) * ((1 << size) * size)
    for vertex in range(size):
        paths[(1 << vertex) * size + vertex] = 1
    totals = [0] * (size + 1)
    for mask in range(1, 1 << size):
        anchor = mask & -mask
        allowed = full ^ ((anchor << 1) - 1)
        length = mask.bit_count()
        endpoints = mask
        while endpoints:
            bit = endpoints & -endpoints
            endpoints ^= bit
            last = bit.bit_length() - 1
            value = paths[mask * size + last]
            if not value:
                continue
            if length >= MIN_CYCLE_LENGTH and adjacency[last] & anchor:
                totals[length] += value
            choices = adjacency[last] & ~mask & allowed
            while choices:
                new_bit = choices & -choices
                choices ^= new_bit
                end = new_bit.bit_length() - 1
                paths[(mask | new_bit) * size + end] += value
    return [value // 2 for value in totals]


def validate(raw):
    parsed = parse_graph(raw)
    if parsed is None:
        return False
    points, adjacency = parsed
    return geometric(points, adjacency) and sum(cycle_histogram(adjacency)) > CYCLE_LIMIT


def main():
    if not validate(Path(sys.argv[3]).read_bytes()):
        print("Invalid planar embedding, matrix or simple-cycle count")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
