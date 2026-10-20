import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = map(int, data[:2])
    board = list(map(int, data[2:-1]))
    program = data[-1]
    directions = b"RDLU"
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    moves = dict(zip(directions, steps))

    def cell(row, col):
        if 0 <= row < n and 0 <= col < m:
            return board[row * m + col]
        return 0

    xs, ys, cost = [0], [0], [board[0]]
    x = y = 0
    for command in program:
        dx, dy = moves[command]
        x += dx
        y += dy
        xs.append(x)
        ys.append(y)
        cost.append(cell(x, y))

    best = source = target = 0
    for direction, (dx, dy) in zip(directions, steps):
        left = right = left_max = right_max = left_at = 0
        right_at = -1
        for i, command in enumerate(program):
            # Prefix maxima choose the best endpoint of a translated path interval.
            if left > left_max:
                left_max, left_at = left, i
            left += cell(xs[i] + dx, ys[i] + dy) - cost[i + 1]
            if command == direction and left - left_max < best:
                best, source, target = left - left_max, i, left_at
            if command == direction and (right_at == -1 or right > right_max):
                right_max, right_at = right, i
            right += cell(xs[i + 1] - dx, ys[i + 1] - dy) - cost[i]
            if right_at != -1 and right - right_max < best:
                best, source, target = right - right_max, right_at, i

    moved = program[source : source + 1]
    remaining = program[:source] + program[source + 1 :]
    sys.stdout.buffer.write(remaining[:target] + moved + remaining[target:] + b"\n")


if __name__ == "__main__":
    main()
