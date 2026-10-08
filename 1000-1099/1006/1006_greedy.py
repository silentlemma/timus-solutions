import sys

WIDTH = 50
HEIGHT = 20
MIN_SIDE = 2
EMPTY = ord(".")
UPPER_LEFT = 218
UPPER_RIGHT = 191
LOWER_LEFT = 192
LOWER_RIGHT = 217
VERTICAL = 179
HORIZONTAL = 196


def border(x, y, side):
    """The cells of a frame with their characters, corners first."""
    last = side - 1
    cells = [
        (x, y, UPPER_LEFT),
        (x + last, y, UPPER_RIGHT),
        (x, y + last, LOWER_LEFT),
        (x + last, y + last, LOWER_RIGHT),
    ]
    for i in range(1, last):
        cells += [
            (x + i, y, HORIZONTAL),
            (x + i, y + last, HORIZONTAL),
            (x, y + i, VERTICAL),
            (x + last, y + i, VERTICAL),
        ]
    return cells


def main():
    rows = sys.stdin.buffer.read().replace(b"\r", b"").split(b"\n")
    rows += [b""] * HEIGHT
    # screen[y][x] is None once the cell is covered by a frame drawn later
    screen = [list(rows[y][:WIDTH].ljust(WIDTH, b".")) for y in range(HEIGHT)]
    left = sum(c != EMPTY for row in screen for c in row)
    frames = [
        (x, y, side)
        for y in range(HEIGHT)
        for x in range(WIDTH)
        for side in range(MIN_SIDE, min(WIDTH - x, HEIGHT - y) + 1)
    ]

    # Undo the drawing: a frame that fits can be the last one drawn among the
    # remaining ones; its cells then may hold anything.
    order = []
    while left > 0:
        before = left
        for x, y, side in frames:
            if screen[y][x] not in (UPPER_LEFT, None):
                continue
            cells = border(x, y, side)
            fresh = 0
            for cx, cy, c in cells:
                got = screen[cy][cx]
                if got is not None:
                    if got != c:
                        break
                    fresh += 1
            else:
                if fresh:
                    order.append((x, y, side))
                    for cx, cy, _ in cells:
                        if screen[cy][cx] is not None:
                            screen[cy][cx] = None
                            left -= 1
        if left == before:
            break

    out = [str(len(order))]
    out += ["%d %d %d" % frame for frame in reversed(order)]
    print("\n".join(out))


main()
