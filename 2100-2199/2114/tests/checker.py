"""Check the optimal sum and the flooded cells of any reported starting cell."""

import sys

RESULT_FIELDS = 3
ARGUMENTS = RESULT_FIELDS + 1
BRUTE_AREA = 400


class Bad(Exception):
    pass


def row_prefixes(grid):
    prefixes = []
    for row in grid:
        prefix = [0]
        for value in row:
            prefix.append(prefix[-1] + value)
        prefixes.append(prefix)
    return prefixes


def flooded(prefixes, row, col, power):
    width = len(prefixes[0]) - 1
    total = 0
    for current in range(row, min(len(prefixes), row + power + 1)):
        end = min(width, col + power - current + row + 1)
        total += prefixes[current][end] - prefixes[current][col]
    return total


def optimal_sum(grid, prefixes, power):
    height, width = len(grid), len(grid[0])
    if power >= height + width - 2:
        return sum(row[-1] for row in prefixes)
    if height * width <= BRUTE_AREA:
        return max(
            flooded(prefixes, row, col, power) for row in range(height) for col in range(width)
        )

    # Moving a triangle down removes its top row and adds one diagonal.
    diagonals = [[0] * (width + 1) for _ in range(height + 1)]
    for row in range(height - 1, -1, -1):
        for col in range(width):
            diagonals[row][col + 1] = grid[row][col] + diagonals[row + 1][col]
    current = [flooded(prefixes, 0, col, power) for col in range(width)]
    best = max(current)
    for row in range(height - 1):
        prefix = prefixes[row]
        for col in range(width):
            diagonal = row + col + power + 1
            first = max(row + 1, diagonal - width + 1)
            last = min(height - 1, row + power + 1)
            added = 0
            if first <= last:
                added = diagonals[first][diagonal - first + 1]
                added -= diagonals[last + 1][diagonal - last]
            removed = prefix[min(width, col + power + 1)] - prefix[col]
            current[col] += added - removed
            best = max(best, current[col])
    return best


def check(source, expected, output):
    del expected
    with open(source, encoding="utf-8") as stream:
        data = list(map(int, stream.read().split()))
    height, width = data[:2]
    end = 2 + height * width
    grid = [data[start : start + width] for start in range(2, end, width)]
    count = data[end]
    powers = data[end + 1 : end + 1 + count]
    with open(output, encoding="utf-8") as stream:
        tokens = stream.read().split()
    if len(tokens) != RESULT_FIELDS * count:
        raise Bad("expected one sum and two coordinates for every query")
    try:
        answers = list(map(int, tokens))
    except ValueError as error:
        raise Bad("the output contains a non-integer token") from error
    prefixes = row_prefixes(grid)
    optimal = {}
    for index, power in enumerate(powers):
        start = index * RESULT_FIELDS
        total, row, col = answers[start : start + RESULT_FIELDS]
        if not 1 <= row <= height or not 1 <= col <= width:
            raise Bad("query %d: coordinates are outside the grid" % (index + 1))
        actual = flooded(prefixes, row - 1, col - 1, power)
        if total != actual:
            raise Bad("query %d: the reported sum does not match its cells" % (index + 1))
        if power not in optimal:
            optimal[power] = optimal_sum(grid, prefixes, power)
        if total != optimal[power]:
            raise Bad("query %d: the flooded sum is not maximal" % (index + 1))


def main():
    try:
        if len(sys.argv) != ARGUMENTS:
            raise Bad("usage: checker.py input expected output")
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
