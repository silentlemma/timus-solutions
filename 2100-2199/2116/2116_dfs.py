import sys


def main():
    n, a, b = map(int, sys.stdin.buffer.read().split())
    if b == 0:
        print(n * n)
        return

    # Each move invariant is connected inside a board of side 2 * b.
    side = min(n, 2 * b)
    moves = []
    for dx in (-a, a):
        for dy in (-b, b):
            moves.append((dx, dy))
            moves.append((dy, dx))

    seen = [False] * (side * side)
    components = 0
    for start in range(side * side):
        if seen[start]:
            continue
        components += 1
        seen[start] = True
        stack = [start]
        while stack:
            cell = stack.pop()
            x, y = divmod(cell, side)
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < side and 0 <= ny < side:
                    next_cell = nx * side + ny
                    if not seen[next_cell]:
                        seen[next_cell] = True
                        stack.append(next_cell)
    print(components)


if __name__ == "__main__":
    main()
