import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grid = [data[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    out = []
    # diagonal s holds the cells with row + column = s; each is read from
    # its lowest row up
    for s in range(2 * n - 1):
        for i in range(min(s, n - 1), max(0, s - n + 1) - 1, -1):
            out.append(grid[i][s - i])
    print(b" ".join(out).decode())


main()
