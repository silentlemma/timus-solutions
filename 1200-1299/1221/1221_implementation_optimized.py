import os
from array import array
import sys

INPUT_BUFFER_BYTES = 4096
WHITESPACE_LIMIT = 32


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > WHITESPACE_LIMIT else b""
        yield from parts
    if pending:
        yield pending


def largest(n, grid):
    # black[i][j]: black cells among the first j of row i
    black = []
    for row in grid:
        acc = array("B", [0])
        for v in row:
            acc.append(acc[-1] + v)
        black.append(acc)

    def ones(i, lo, hi):
        """Black cells of row i in columns lo..hi."""
        return black[i][hi + 1] - black[i][lo]

    def fits(ci, cj, r):
        # row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
        for d in range(-r, r + 1):
            i, side = ci + d, abs(d)
            left, right = cj - r, cj + r
            inner = r - side
            if ones(i, left, cj - inner - 1) != side or ones(i, cj + inner + 1, right) != side:
                return False
            if ones(i, cj - inner, cj + inner):
                return False
        return True

    # the white square needs a cell on every side of the centre, so r >= 1
    for r in range((n - 1) // 2, 0, -1):
        for ci in range(r, n - r):
            top, mid = grid[ci - r], grid[ci]
            for cj in range(r, n - r):
                # quick tests first: a white centre and tip, a black corner
                if mid[cj] or top[cj] or not top[cj - r]:
                    continue
                if fits(ci, cj, r):
                    return 2 * r + 1
    return 0


def main():
    tokens = words()
    out = []
    while True:
        n = int(next(tokens))
        if n == 0:
            break
        # the cells may come with or without spaces between them
        cells = bytearray()
        while len(cells) < n * n:
            cells.extend(c - ord("0") for c in next(tokens))
        grid = [cells[i * n : (i + 1) * n] for i in range(n)]
        best = largest(n, grid)
        out.append(str(best) if best else "No solution")
    print("\n".join(out))


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
