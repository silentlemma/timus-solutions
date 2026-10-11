import sys

FIELDS = 5  # W, H, X, Y and D
OPEN = bytes(0 if ch == ord("#") else 1 for ch in range(256))


def main():
    words = iter(sys.stdin.buffer.read().split())
    w, h, x, y, d = (int(next(words)) for _ in range(FIELDS))
    # a frame of rock around the cave saves every bounds check
    width = w + 2
    rock = b"#" * width
    grid = rock + b"".join(b"#" + next(words)[:w] + b"#" for _ in range(h)) + rock
    open_cell = grid.translate(OPEN)
    first = width + 1  # the left end of the top row
    # water reaches a cell that has a way to the surface without going down,
    # so search back from the top row: down, left and right
    wet = bytearray(len(grid))
    stack = [first + c for c in range(w) if open_cell[first + c]]
    for cell in stack:
        wet[cell] = 1
    while stack:
        cell = stack.pop()
        for nxt in (cell + width, cell - 1, cell + 1):
            if open_cell[nxt] and not wet[nxt]:
                wet[nxt] = 1
                stack.append(nxt)
    # label: moves made under water since the last breath; an air pocket
    # resets it to 0, and no stretch under water may take more than D moves
    start = (h - y + 1) * width + x
    label = [d + 1] * len(grid)
    label[start] = 0
    buckets = [[] for _ in range(d + 1)]
    buckets[0].append(start)
    top_row_end = first + w
    level = 0
    while level <= d:
        bucket = buckets[level]
        if not bucket:
            level += 1
            continue
        cell = bucket.pop()
        here = label[cell]
        if here != level:
            continue
        if cell < top_row_end and here < d:
            print("Can be rescued by himself")
            return
        cell_wet = wet[cell]
        for nxt in (cell - width, cell + width, cell - 1, cell + 1):
            if not open_cell[nxt]:
                continue
            if wet[nxt]:
                new = here + 1
            elif cell_wet and here >= d:
                continue
            else:
                new = 0
            if new <= d and new < label[nxt]:
                label[nxt] = new
                buckets[new].append(nxt)
                if new < level:
                    level = new
    print("Rescue operation required")


main()
