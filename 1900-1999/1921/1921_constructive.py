import sys


def construct_board(rows, columns, palette, level):
    target = level - 1
    longest = max(rows, columns)
    if longest < target:
        return None
    if palette == 1:
        return ["A" * columns for _ in range(rows)] if longest == target else None
    if target == 1:
        column_colors = min(columns, 2)
        if palette < min(rows, 2) * column_colors:
            return None
        return [
            "".join(
                chr(ord("A") + (row % 2) * column_colors + column % 2)
                for column in range(columns)
            )
            for row in range(rows)
        ]
    if columns >= target:
        return [
            "".join(
                chr(ord("A") + (row + column // target) % 2)
                for column in range(columns)
            )
            for row in range(rows)
        ]
    return [
        "".join(
            chr(ord("A") + (column + row // target) % 2) for column in range(columns)
        )
        for row in range(rows)
    ]


def main():
    rows, columns, palette, level = map(int, sys.stdin.buffer.read().split())
    board = construct_board(rows, columns, palette, level)
    if board is None:
        print("NO")
    else:
        print("YES")
        print("\n".join(board))


if __name__ == "__main__":
    main()
