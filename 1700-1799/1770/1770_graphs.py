import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [[int(data[1 + i * n + j]) for j in range(n)] for i in range(n)]
    # every road must cost at least the table in both directions, so the
    # cheapest roads allowed are taken: a free road where the table says 0
    # both ways, a road with a board seen from i where it says 1 and 0
    free = [0] * n
    board = [0] * n
    grid = [["0"] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and a[i][j] + a[j][i] <= 1:
                if a[i][j]:
                    board[i] |= 1 << j
                    grid[i][j] = "2"
                else:
                    free[i] |= 1 << j
                    grid[i][j] = "1"
    # these roads give the smallest costs any network can have, so the table
    # is right exactly when they give it; the costs are found level by level,
    # with the vertices of one cost as a bit mask
    full = (1 << n) - 1
    for s in range(n):
        want = [0] * n
        for j, cost in enumerate(a[s]):
            want[cost] |= 1 << j
        seen = 0
        level = 1 << s
        for cost in range(n):
            if seen == full:
                break
            frontier = level & ~seen
            reached = 0
            while frontier:
                reached |= frontier
                seen |= frontier
                spread = 0
                while frontier:
                    low = frontier & -frontier
                    spread |= free[low.bit_length() - 1]
                    frontier ^= low
                frontier = spread & ~seen
            if reached != want[cost]:
                print("NO")
                return
            level = 0
            while reached:
                low = reached & -reached
                level |= board[low.bit_length() - 1]
                reached ^= low
    print("YES")
    print("\n".join("".join(row) for row in grid))


main()
