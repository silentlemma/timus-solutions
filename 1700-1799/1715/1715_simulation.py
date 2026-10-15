import sys

COLORS = "BGRWY"
EMPTY = "."


def best_figure(board, n, m, main, take_main):
    # the largest figure of the main colour or of the others; ties go to the
    # figure holding the lowest ball, then the leftmost of the lowest balls
    seen = [False] * (n * m)
    best = None
    best_key = None
    for start in range(n * m):
        color = board[start]
        if seen[start] or color == EMPTY or (color == main) != take_main:
            continue
        seen[start] = True
        cells = [start]
        low = start
        k = 0
        while k < len(cells):
            v = cells[k]
            k += 1
            r, c = divmod(v, m)
            if r > low // m or (r == low // m and c < low % m):
                low = v
            for w, ok in ((v - m, r > 0), (v + m, r < n - 1), (v - 1, c > 0), (v + 1, c < m - 1)):
                if ok and not seen[w] and board[w] == color:
                    seen[w] = True
                    cells.append(w)
        if len(cells) >= 2:
            key = (len(cells), low // m, -(low % m))
            if best_key is None or key > best_key:
                best, best_key = cells, key
    return best


def remove(board, n, m, cells):
    for v in cells:
        board[v] = EMPTY
    # balls fall down, then empty columns close up to the left
    columns = []
    for c in range(m):
        column = [board[r * m + c] for r in range(n) if board[r * m + c] != EMPTY]
        if column:
            columns.append([EMPTY] * (n - len(column)) + column)
    for c in range(m):
        column = columns[c] if c < len(columns) else [EMPTY] * n
        for r in range(n):
            board[r * m + c] = column[r]
    return len(cells) * (len(cells) - 1)


def play(start, n, m, main):
    board = list(start)
    score = 0
    while True:
        while True:
            cells = best_figure(board, n, m, main, False)
            if cells is None:
                break
            score += remove(board, n, m, cells)
        cells = best_figure(board, n, m, main, True)
        if cells is None:
            return score
        score += remove(board, n, m, cells)


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    board = "".join(data[2:2 + n])
    out = []
    for color in COLORS:
        if color in board:
            out.append("%s: %d" % (color, play(board, n, m, color)))
    print("\n".join(out))


main()
