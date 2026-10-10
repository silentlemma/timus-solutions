import re
import sys

# beacons and control points lie on the grid from 1 to SIDE
SIDE = 200


def ring(x, y, r):
    # the cells at distance exactly r from (x, y) in the max metric
    if r == 0:
        return [(x, y)]
    cells = [(x + d, y + s) for d in range(-r, r + 1) for s in (-r, r)]
    cells += [(x + s, y + d) for d in range(-r + 1, r) for s in (-r, r)]
    return cells


def main():
    lines = [line for line in sys.stdin.read().split("\n") if line.strip()]
    m = int(lines[0])
    seen = {}
    for line in lines[1 : 1 + m]:
        nums = list(map(int, re.findall(r"\d+", line)))
        x, y = nums[0], nums[1]
        for k in range(2, len(nums), 2):
            seen.setdefault(nums[k], []).append((x, y, nums[k + 1]))
    out = []
    for beacon in sorted(seen):
        (x, y, r), *rest = seen[beacon]
        places = [
            (cx, cy)
            for cx, cy in ring(x, y, r)
            if 1 <= cx <= SIDE
            and 1 <= cy <= SIDE
            and all(max(abs(cx - px), abs(cy - py)) == pr for px, py, pr in rest)
        ]
        if len(places) == 1:
            out.append("%d:%d,%d" % (beacon, places[0][0], places[0][1]))
        else:
            out.append("%d:UNKNOWN" % beacon)
    sys.stdout.write("\n".join(out) + "\n")


main()
