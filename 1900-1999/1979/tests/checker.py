"""Validate the complete cube permutation and trace every opposite-edge cycle."""

from collections import deque
from pathlib import Path
import sys

NET = ((0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0))


def neg(v):
    return tuple(-x for x in v)


def orientations():
    poses = {(1, 0): ((0, 0, 1), (1, 0, 0), (0, -1, 0))}
    pending = deque([(1, 0)])
    while pending:
        row, col = pending.popleft()
        normal, u, v = poses[row, col]
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nxt = (row + dr, col + dc)
            if nxt not in NET or nxt in poses:
                continue
            if dc == 1:
                orient = (u, neg(normal), v)
            elif dc == -1:
                orient = (neg(u), normal, v)
            elif dr == 1:
                orient = (v, u, neg(normal))
            else:
                orient = (neg(v), u, normal)
            poses[nxt] = orient
            pending.append(nxt)
    assert len(poses) == 6 and len({p[0] for p in poses.values()}) == 6
    return [poses[p] for p in NET]


def verify(n, text):
    lines = text.splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    if len(lines) != 3 * n:
        return False, "wrong number of net rows"
    rows = []
    try:
        for r, line in enumerate(lines):
            row = list(map(int, line.split()))
            width = 4 * n if n <= r < 2 * n else n
            if len(row) != width:
                return False, "wrong net row width"
            rows.append(row)
    except ValueError:
        return False, "non-integer output"
    values = []
    for face, (fr, fc) in enumerate(NET):
        for r in range(n):
            start = fc * n if fr == 1 else 0
            values.extend(rows[fr * n + r][start : start + n])
    total = 6 * n * n
    if len(values) != total or set(values) != set(range(1, total + 1)):
        return False, "labels must be exactly1..6n^2"
    poses = orientations()
    centers = []
    directions = []
    for normal, u, v in poses:
        directions.append((u, v, neg(u), neg(v)))
        for r in range(n):
            for c in range(n):
                centers.append(
                    tuple(
                        normal[a] * n + u[a] * (2 * c + 1 - n) + v[a] * (2 * r + 1 - n)
                        for a in range(3)
                    )
                )
    by_center = {point: i for i, point in enumerate(centers)}
    if len(by_center) != total:
        return False, "invalid cube folding"
    seen = bytearray(4 * total)
    target = 2 * n * (total + 1)
    cycles = 0
    for start in range(4 * total):
        if seen[start]:
            continue
        state = start
        length = amount = 0
        while not seen[state]:
            seen[state] = 1
            cell, direction = divmod(state, 4)
            face, within = divmod(cell, n * n)
            row, col = divmod(within, n)
            amount += values[cell]
            length += 1
            dr, dc = ((0, 1), (1, 0), (0, -1), (-1, 0))[direction]
            if 0 <= row + dr < n and 0 <= col + dc < n:
                state = 4 * (cell + dr * n + dc) + direction
            else:
                normal = poses[face][0]
                travel = directions[face][direction]
                center = centers[cell]
                nxt = tuple(center[a] + travel[a] - normal[a] for a in range(3))
                next_cell = by_center[nxt]
                next_face = next_cell // (n * n)
                next_direction = directions[next_face].index(neg(normal))
                state = 4 * next_cell + next_direction
        if state != start or length != 4 * n:
            return False, "opposite-edge path did not form its required cycle"
        if amount != target:
            return False, "unequal resource sum on a cube cycle"
        cycles += 1
    return cycles == 6 * n, "OK" if cycles == 6 * n else "missing cycles"


if __name__ == "__main__":
    try:
        n = int(Path(sys.argv[1]).read_text().strip())
        assert 1 <= n <= 100
        passed, detail = verify(n, Path(sys.argv[3]).read_text())
    except (ValueError, IndexError, KeyError, AssertionError, OSError) as error:
        passed, detail = False, str(error)
    print(detail)
    raise SystemExit(0 if passed else 1)
