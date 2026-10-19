import sys


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    rows = next(values)
    columns = next(values)
    diagonal_count = rows + columns - 1
    row_prefix = []
    column_prefix = [[0] * columns]
    diagonals = [[0] * (rows + 1) for _ in range(diagonal_count)]
    total = 0
    for row in range(rows):
        prefix = [0]
        column_sums = []
        above = column_prefix[-1]
        running = 0
        for column in range(columns):
            value = next(values)
            running += value
            prefix.append(running)
            column_sums.append(above[column] + value)
            diagonals[row + column][row + 1] = value
        row_prefix.append(prefix)
        column_prefix.append(column_sums)
        total += running

    for diagonal in diagonals:
        running = 0
        for row in range(rows):
            running += diagonal[row + 1]
            diagonal[row + 1] = running
    diagonals += [[0] * (rows + 1)] * diagonal_count

    queries = next(values)
    answers = {}
    output = []
    maximum_distance = rows + columns - 2
    for _ in range(queries):
        wind = next(values)
        if wind in answers:
            output.append(answers[wind])
            continue
        if wind >= maximum_distance:
            answer = f"{total} 1 1"
        else:
            below = [0] * columns
            first_right = min(columns, wind + 1)
            repeated_right = min(wind, columns - 1)
            best = -1
            best_row = best_column = 0
            for row in range(rows - 1, -1, -1):
                prefix = row_prefix[row]
                first = row + 1
                last = min(rows, row + wind + 2)
                diagonal_start = row + wind + 1
                diagonal = diagonals[diagonal_start]
                left = below[0] + prefix[first_right] - diagonal[last] + diagonal[first]
                right_values = prefix[wind + 2 :] + [prefix[-1]] * repeated_right
                # Shifting up and right preserves the far diagonal.
                below = [left] + [
                    old + end - start - bottom + top
                    for old, end, start, bottom, top in zip(
                        below,
                        right_values,
                        prefix[1:],
                        column_prefix[last],
                        column_prefix[first],
                    )
                ]
                row_best = max(below)
                # Later rows in this traversal are earlier in row order.
                if row_best >= best:
                    best = row_best
                    best_row = row
                    best_column = below.index(row_best)
            answer = f"{best} {best_row + 1} {best_column + 1}"
        answers[wind] = answer
        output.append(answer)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
