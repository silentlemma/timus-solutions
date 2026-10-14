import sys

OPEN, CLOSE = 1, 2  # the ends of a path piece, matched like brackets
FLIP = OPEN ^ CLOSE  # turns one end into the other
BITS = 2  # bits per plug
MASK = 3


def partner(state, pos, step):
    """The plug matching the bracket at pos, searching towards step."""
    depth = 0
    while True:
        v = state >> (BITS * pos) & MASK
        if v == OPEN:
            depth += step
        elif v == CLOSE:
            depth -= step
        if depth == 0:
            return pos
        pos += step


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2 : 2 + n]
    free = [[ch == "." for ch in row] + [False] for row in grid] + [[False] * (m + 1)]
    last = max(i * m + j for i in range(n) for j in range(m) if free[i][j])

    # a state holds m + 1 plugs: plug j is the left side of the current cell
    # when j is its column, plug j + 1 its upper side; the rest are the lower
    # sides of the row above or this row
    ways = {0: 1}
    total = 0
    for i in range(n):
        for j in range(m):
            nxt = {}
            get = nxt.get
            sl, su = BITS * j, BITS * (j + 1)
            clear = ~(MASK << sl) & ~(MASK << su)
            down, right = free[i + 1][j], free[i][j + 1]
            if not free[i][j]:
                for state, count in ways.items():
                    if not state >> sl & (MASK | MASK << BITS):
                        nxt[state] = count
                ways = nxt
                continue
            for state, count in ways.items():
                left, up = state >> sl & MASK, state >> su & MASK
                base = state & clear
                if left == 0 and up == 0:
                    if down and right:
                        out = base | OPEN << sl | CLOSE << su
                        nxt[out] = get(out, 0) + count
                elif left == 0 or up == 0:
                    end = left | up
                    if down:
                        out = base | end << sl
                        nxt[out] = get(out, 0) + count
                    if right:
                        out = base | end << su
                        nxt[out] = get(out, 0) + count
                elif left == up:
                    # two openings or two closings: the far end of one of
                    # the joined pieces changes its kind
                    if left == OPEN:
                        far = partner(state, j + 1, 1)
                    else:
                        far = partner(state, j, -1)
                    out = base ^ FLIP << (BITS * far)
                    nxt[out] = get(out, 0) + count
                elif left == CLOSE:
                    nxt[base] = get(base, 0) + count
                elif i * m + j == last and base == 0:
                    total += count  # the loop closes on the last free cell
            ways = nxt
        # the next row starts with an empty left plug
        ways = {state << BITS: count for state, count in ways.items()}
    print(total)


main()
