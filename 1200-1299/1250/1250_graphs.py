import sys

HEADER = 4
FLIP = bytes.maketrans(bytes([0, 1]), bytes([1, 0]))


def flood(start, free, steps):
    """Marks in free (setting it to 0) and returns every cell reachable from
    start through cells where free is 1, moving along the given steps."""
    size = len(free)
    reached = [start]
    free[start] = 0
    stack = [start]
    while stack:
        c = stack.pop()
        for d in steps:
            n = c + d
            if 0 <= n < size and free[n]:
                free[n] = 0
                reached.append(n)
                stack.append(n)
    return reached


def main():
    data = sys.stdin.buffer.read()
    head = data.split(maxsplit=HEADER)
    w, h, x, y = map(int, head[:HEADER])
    cells = bytes(c for c in head[HEADER] if c in b".#") if len(head) > HEADER else b""
    # the map padded by a ring of outside cells
    pw = w + 2
    land = bytearray((w + 2) * (h + 2))
    sea = bytearray(len(land))
    for i in range(h):
        row = cells[i * w : (i + 1) * w]
        at = (i + 1) * pw + 1
        land[at : at + w] = row.replace(b"#", b"\1").replace(b".", b"\0")
        sea[at : at + w] = row.replace(b"#", b"\0").replace(b".", b"\1")
    step4 = (1, -1, pw, -pw)
    step8 = step4 + (pw + 1, pw - 1, -pw + 1, -pw - 1)
    # the sacred sea: sea cells joined to the drowning point by 8 directions
    sacred = bytearray(len(land))
    start = y * pw + x
    if sea[start]:
        for c in flood(start, sea, step8):
            sacred[c] = 1
    # an eight-connected sea stops every four-connected path, so what the
    # outside cannot reach without crossing the sacred sea lies inside it
    free = sacred.translate(FLIP)
    for c in flood(0, free, step4):
        land[c] = 0
    count = 0
    for c in range(len(land)):
        if land[c]:
            count += 1
            flood(c, land, step4)
    print(count)


main()
