def main():
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    number = 1
    # diagonals by column minus row, from the top right corner down
    for shift in range(n - 1, -n, -1):
        for row in range(max(0, -shift), min(n, n - shift)):
            grid[row][row + shift] = number
            number += 1
    print("\n".join(" ".join(map(str, line)) for line in grid))


main()
