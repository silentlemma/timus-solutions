import sys


def is_unimodular(matrix):
    size = len(matrix)
    values = [row[:] for row in matrix]
    previous = 1
    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if values[row][column] != 0), None
        )
        if pivot_row is None:
            return False
        values[column], values[pivot_row] = values[pivot_row], values[column]
        pivot_line = values[column]
        pivot = pivot_line[column]
        for row in range(column + 1, size):
            line = values[row]
            factor = line[column]
            for target in range(column + 1, size):
                line[target] = (
                    line[target] * pivot - factor * pivot_line[target]
                ) // previous
            line[column] = 0
        previous = pivot
    return abs(values[-1][-1]) == 1


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    size = next(tokens)
    matrix = [[next(tokens) for _ in range(size)] for _ in range(size)]
    print("Death" if is_unimodular(matrix) else "Power of magic saves lives")


if __name__ == "__main__":
    main()
