import sys


def territory_sizes(board, moves):
    rows, columns = len(board), len(board[0])
    cells = rows * columns
    colors = [int(letter) for line in board for letter in line]
    neighbors = [[] for _ in range(cells)]
    for row in range(rows):
        for column in range(columns):
            cell = row * columns + column
            if row:
                neighbors[cell].append(cell - columns)
            if row + 1 < rows:
                neighbors[cell].append(cell + columns)
            if column:
                neighbors[cell].append(cell - 1)
            if column + 1 < columns:
                neighbors[cell].append(cell + 1)
    owners = [-1] * cells
    territories = [[], []]

    def expand(player, color):
        # Appended cells are visited in this same pass through the growing list.
        for cell in territories[player]:
            for adjacent in neighbors[cell]:
                if owners[adjacent] == -1 and colors[adjacent] == color:
                    owners[adjacent] = player
                    territories[player].append(adjacent)

    for player, seed in enumerate((cells - columns, columns - 1)):
        owners[seed] = player
        territories[player].append(seed)
        expand(player, colors[seed])
    for turn, color in enumerate(moves):
        expand(turn % 2, color)
    return len(territories[0]), len(territories[1])


def main():
    tokens = sys.stdin.buffer.read().split()
    rows = int(tokens[0])
    board = [line.decode() for line in tokens[2 : rows + 2]]
    count = int(tokens[rows + 2])
    move_start = rows + 2 + 1
    moves = list(map(int, tokens[move_start : move_start + count]))
    first, second = territory_sizes(board, moves)
    print(first)
    print(second)


if __name__ == "__main__":
    main()
