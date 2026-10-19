from math import isqrt
import sys

SMALL_ODD_LIMIT = 5
FIRST_ODD_PRIME = 3
COLUMN = 2


def construct(n):
    grid = [[0] * n for _ in range(n)]
    value = 0

    def visit(row, col):
        nonlocal value
        value += 1
        grid[row][col] = value

    if n % 2 and n < SMALL_ODD_LIMIT:
        for row in range(n):
            columns = range(n) if row % 2 == 0 else range(n - 1, -1, -1)
            for col in columns:
                visit(row, col)
        return grid

    limit = n * n
    prime = bytearray(b"\1") * (limit + 1)
    prime[:2] = b"\0\0"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p * p :: p] = b"\0" * ((limit - p * p) // p + 1)
    following = [0] * (limit + 1)
    largest = 0
    for p in range(limit, -1, -1):
        following[p] = largest
        if prime[p]:
            largest = p
    widths = [0] * n

    if n % 2 == 0:
        visit(0, 1)
        visit(0, 0)
        visit(1, 0)
        for row in range(1, n - 2, 2):
            width = (following[value] - value - 2) // 2
            widths[row] = width
            for col in range(1, width + 1):
                visit(row, col)
            visit(row + 1, width)
            for col in range(width - 1, -1, -1):
                visit(row + 1, col)
            visit(row + 2, 0)
        for col in range(1, n):
            visit(n - 1, col)
        for row in range(n - 2, 1, -2):
            width = widths[row - 1]
            for col in range(n - 1, width, -1):
                visit(row, col)
            for col in range(width + 1, n):
                visit(row - 1, col)
        for col in range(n - 1, 1, -1):
            visit(0, col)
        return grid

    right_width = n - COLUMN - 1
    initial = None
    for candidate in range(right_width + 1):
        if candidate == right_width - 1:
            continue
        first = FIRST_ODD_PRIME + 2 * candidate
        current = first + 2 * n
        if not prime[first] or not prime[current]:
            continue
        for row in range(n - 1, COLUMN + 1, -2):
            next_prime = following[current]
            width = (next_prime - current - 2) // 2
            if not 0 <= width < right_width:
                break
            widths[row] = width
            current = next_prime
        else:
            initial = candidate
            break
    if initial is None:
        raise ValueError("No admissible prime prefix")

    visit(1, 1)
    visit(1, COLUMN)
    for col in range(COLUMN + 1, COLUMN + initial + 1):
        visit(1, col)
    for col in range(COLUMN + initial, COLUMN - 1, -1):
        visit(0, col)
    visit(0, 1)
    visit(0, 0)
    visit(1, 0)
    visit(2, 0)
    visit(2, 1)
    for row in range(COLUMN + 1, n, 2):
        visit(row, 1)
        visit(row, 0)
        visit(row + 1, 0)
        visit(row + 1, 1)
    visit(n - 1, COLUMN)
    for row in range(n - 1, COLUMN + 1, -2):
        width = widths[row]
        for col in range(COLUMN + 1, COLUMN + width + 1):
            visit(row, col)
        visit(row - 1, COLUMN + width)
        for col in range(COLUMN + width - 1, COLUMN - 1, -1):
            visit(row - 1, col)
        visit(row - 2, COLUMN)

    left = COLUMN + initial + 1
    if left == n:
        for col in range(COLUMN + 1, n):
            visit(2, col)
    else:
        for col in range(COLUMN + 1, left + 1):
            visit(2, col)
        visit(1, left)
        for col in range(left, n):
            visit(0, col)
        for col in range(n - 1, left, -1):
            visit(1, col)
        for col in range(left + 1, n):
            visit(2, col)
    for row in range(COLUMN + 1, n, 2):
        width = widths[row + 1]
        for col in range(n - 1, COLUMN + width, -1):
            visit(row, col)
        for col in range(COLUMN + width + 1, n):
            visit(row + 1, col)
    return grid


def main():
    n = int(sys.stdin.buffer.read())
    print("\n".join(" ".join(map(str, row)) for row in construct(n)))


if __name__ == "__main__":
    main()
