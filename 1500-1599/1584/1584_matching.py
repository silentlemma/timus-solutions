import sys

CORNERS = 4  # cells in a group of mirror positions
INF = float("inf")


def hungarian(cost):
    """The least total cost of giving each row its own column of a square
    matrix, by the potentials method in O(n^3)."""
    n = len(cost)
    u, v = [0] * (n + 1), [0] * (n + 1)
    owner = [0] * (n + 1)  # the row that holds each column, 0 for none
    for row in range(1, n + 1):
        owner[0] = row
        col0 = 0
        least = [INF] * (n + 1)
        prev = [0] * (n + 1)
        used = [False] * (n + 1)
        while owner[col0]:
            used[col0] = True
            r = owner[col0]
            delta, col1 = INF, 0
            line = cost[r - 1]
            ur = u[r]
            for c in range(1, n + 1):
                if not used[c]:
                    reduced = line[c - 1] - ur - v[c]
                    if reduced < least[c]:
                        least[c], prev[c] = reduced, col0
                    if least[c] < delta:
                        delta, col1 = least[c], c
            for c in range(n + 1):
                if used[c]:
                    u[owner[c]] += delta
                    v[c] -= delta
                else:
                    least[c] -= delta
            col0 = col1
        while col0:
            col1 = prev[col0]
            owner[col0] = owner[col1]
            col0 = col1
    return -v[0]


def main():
    words = sys.stdin.read().split()
    n, m = int(words[0]), int(words[1])
    grid = words[2 : 2 + n]
    # every row and column symmetric means the four mirror images of a cell
    # hold one kind of statue; each group then gets one kind
    groups = []
    for i in range(n // 2):
        for j in range(m // 2):
            cells = (
                grid[i][j] + grid[i][m - 1 - j] + grid[n - 1 - i][j] + grid[n - 1 - i][m - 1 - j]
            )
            groups.append(cells)
    total = "".join(grid)
    # a kind with c statues fills c / 4 groups; one column per such place
    slots = [k for k in sorted(set(total)) for _ in range(total.count(k) // CORNERS)]
    # a statue not already in place is carried once, and a cycle of k statues
    # takes k carries, so the answer is the number of statues that change
    cost = [[CORNERS - g.count(k) for k in slots] for g in groups]
    print(hungarian(cost))


main()
