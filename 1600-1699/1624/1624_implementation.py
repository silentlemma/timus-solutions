import sys

STEP = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
SAFE = "The scouts are safe at step number %d"
UNKNOWN = "There is not enough data"
MISTAKE = "A mistake has been made at step number %d"


def edge(r, c, d):
    """the wall or door crossed from cell (r, c) in direction d: horizontal
    edges (kind 0) above row r, vertical ones (kind 1) left of column c"""
    if d == "N":
        return (0, r, c)
    if d == "S":
        return (0, r + 1, c)
    if d == "W":
        return (1, r, c)
    return (1, r, c + 1)


class Scout:
    def __init__(self):
        self.r = self.c = 0  # the position relative to the unknown start
        self.lo_r = self.hi_r = self.lo_c = self.hi_c = 0
        self.seen = {}  # edge -> 1 for a door, 0 for a wall
        self.by_kind = [[[], []], [[], []]]  # [kind][door?]: the edges seen


def main():
    data = sys.stdin.read().split()
    w, h, k = int(data[0]), int(data[1]), int(data[2])
    scouts = [Scout(), Scout()]
    # conflict[dr][dc]: the reports that rule out the second start being
    # the first one shifted by (dr, dc), the same edge seen differently
    width = 2 * w - 1
    conflict = [0] * ((2 * h - 1) * width)

    def starts():
        """the start pairs left: 0, 1, or 2 for two or more"""
        a, b = scouts
        lo1r, hi1r, lo1c, hi1c = -a.lo_r, h - 1 - a.hi_r, -a.lo_c, w - 1 - a.hi_c
        lo2r, hi2r, lo2c, hi2c = -b.lo_r, h - 1 - b.hi_r, -b.lo_c, w - 1 - b.hi_c
        total = 0
        for dr in range(-(h - 1), h):
            top, bottom = max(lo1r, lo2r - dr), min(hi1r, hi2r - dr)
            if top > bottom:
                continue
            row = (dr + h - 1) * width + w - 1
            for dc in range(-(w - 1), w):
                if conflict[row + dc]:
                    continue
                left, right = max(lo1c, lo2c - dc), min(hi1c, hi2c - dc)
                if left <= right:
                    total += (bottom - top + 1) * (right - left + 1)
                    if total > 1:
                        return 2
        return total

    safe = -1
    count = starts()
    for step in range(1, k + 1):
        report = data[2 + step]
        d, door = report[0], 1 if report[1] == "+" else 0
        who = (step - 1) % 2
        me, other = scouts[who], scouts[1 - who]
        e = edge(me.r, me.c, d)
        changed = False
        old = me.seen.get(e)
        if old is None:
            me.seen[e] = door
            me.by_kind[e[0]][door].append(e)
            # the other scout's opposite reports about edges of this kind
            sign = 1 if who == 0 else -1
            for f in other.by_kind[e[0]][1 - door]:
                dr, dc = sign * (e[1] - f[1]), sign * (e[2] - f[2])
                if -h < dr < h and -w < dc < w:
                    conflict[(dr + h - 1) * width + dc + w - 1] += 1
                    changed = True
        elif old != door:
            print(MISTAKE % step)
            return
        if door:
            dr, dc = STEP[d]
            me.r += dr
            me.c += dc
            if not me.lo_r <= me.r <= me.hi_r or not me.lo_c <= me.c <= me.hi_c:
                me.lo_r, me.hi_r = min(me.lo_r, me.r), max(me.hi_r, me.r)
                me.lo_c, me.hi_c = min(me.lo_c, me.c), max(me.hi_c, me.c)
                changed = True
        if changed:  # the count changes only with a new conflict or a wider path
            count = starts()
        if count == 0:
            print(MISTAKE % step)
            return
        if count == 1 and safe < 0:
            safe = step
    print(SAFE % safe if safe > 0 else UNKNOWN)


main()
