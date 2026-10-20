import sys
from bisect import bisect_left, bisect_right

FULL_TURN = 4
THREE_QUARTERS = FULL_TURN - 1
TURNS = {b"r90": 1, b"r180": 2, b"r270": THREE_QUARTERS}


def main():
    data = iter(sys.stdin.buffer.read().split())
    n = int(next(data))
    points = [(int(next(data)), int(next(data))) for _ in range(n)]
    points.sort()
    ys = sorted({y for _, y in points})
    events = []
    answers = []
    tx = ty = orientation = 0
    for _ in range(int(next(data))):
        command = next(data)
        x, y = int(next(data)), int(next(data))
        if command != b"ask":
            turns = TURNS[command]
            dx, dy = tx - x, ty - y
            for _ in range(turns):
                dx, dy = -dy, dx
            tx, ty = x + dx, y + dy
            orientation = (orientation + turns) % FULL_TURN
        else:
            xx, yy = int(next(data)), int(next(data))
            x, y, xx, yy = x - tx, y - ty, xx - tx, yy - ty
            # Undo the global transform on two opposite corners.
            for _ in range(orientation):
                x, y, xx, yy = y, -x, yy, -xx
            if x > xx:
                x, xx = xx, x
            if y > yy:
                y, yy = yy, y
            index = len(answers)
            answers.append(0)
            events.append((xx, y, yy, index, 1))
            events.append((x - 1, y, yy, index, -1))

    events.sort()
    size = len(ys)
    tree = [0] * (size + 1)
    inserted = 0
    for x, low, high, answer, sign in events:
        while inserted < n and points[inserted][0] <= x:
            index = bisect_left(ys, points[inserted][1]) + 1
            while index <= size:
                tree[index] += 1
                index += index & -index
            inserted += 1
        count = 0
        index = bisect_right(ys, high)
        while index:
            count += tree[index]
            index -= index & -index
        index = bisect_left(ys, low)
        while index:
            count -= tree[index]
            index -= index & -index
        answers[answer] += sign * count
    if answers:
        sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
