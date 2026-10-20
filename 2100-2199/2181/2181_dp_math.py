import sys

MOD = 1_000_000_007


def count_paths(rows, columns, blocked_above, blocked_left, start_row, start_column):
    ways = [0] * columns
    upper = 0
    for row in range(start_row, rows):
        offset = row * columns
        for column in range(start_column, columns):
            position = offset + column
            if row == start_row and column == start_column:
                ways[column] = 1
                continue
            value = 0 if blocked_above[position] else ways[column]
            if column > start_column and not blocked_left[position]:
                value += ways[column - 1]
            if value >= MOD:
                value -= MOD
            ways[column] = value
        if row == rows - 2:
            upper = ways[-1]
    return upper, ways[-2]


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    rows = next(data)
    columns = next(data)
    missing = next(data)
    blocked_above = bytearray(rows * columns)
    blocked_left = bytearray(rows * columns)
    for _ in range(missing):
        first_row = next(data) - 1
        first_column = next(data) - 1
        second_row = next(data) - 1
        second_column = next(data) - 1
        if first_row == second_row:
            blocked_left[first_row * columns + max(first_column, second_column)] = 1
        else:
            blocked_above[max(first_row, second_row) * columns + first_column] = 1

    if blocked_left[1] or blocked_above[columns] or blocked_left[-1] or blocked_above[-1]:
        print(0)
        return

    upper_upper, upper_lower = count_paths(rows, columns, blocked_above, blocked_left, 0, 1)
    lower_upper, lower_lower = count_paths(rows, columns, blocked_above, blocked_left, 1, 0)
    # Tail swapping cancels intersecting path pairs in this determinant.
    answer = (upper_upper * lower_lower - upper_lower * lower_upper) % MOD
    print(2 * answer % MOD)


if __name__ == "__main__":
    main()
