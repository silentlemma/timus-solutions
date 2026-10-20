import sys


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, a, b = next(values), next(values), next(values), next(values)
    row_total = 0
    selected_row = 0
    for i in range(1, n + 1):
        value = next(values)
        row_total += value
        if i == a:
            selected_row = value
    column_total = 0
    selected_column = 0
    for j in range(1, m + 1):
        value = next(values)
        column_total += value
        if j == b:
            selected_column = value

    if row_total != column_total:
        print(0)
        return
    lower = max(0, selected_row + selected_column - row_total)
    upper = min(selected_row, selected_column)
    print(upper - lower + 1)


if __name__ == "__main__":
    main()
