import sys


def main():
    n = int(sys.stdin.buffer.read())
    for row in range(n):
        cells = []
        for col in range(n):
            # the diagonal of this cell has n - |col - row| cells; above the main
            # one count the earlier diagonals, below it count from the end
            length = n - abs(col - row)
            if col >= row:
                value = length * (length - 1) // 2 + row + 1
            else:
                value = n * n - length * (length + 1) // 2 + col + 1
            cells.append(str(value))
        sys.stdout.write(" ".join(cells) + "\n")


main()
