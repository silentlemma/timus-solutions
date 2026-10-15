import sys

HEADER = 3  # n, d and a come before the matrix


def main():
    data = sys.stdin.read().split()
    n, d, a = int(data[0]), int(data[1]), int(data[2])
    flights = data[HEADER:HEADER + n]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # the result must be a spanning tree: keep a spanning forest of the
    # existing flights, cancel the rest, then join the trees with new flights
    plan = [["0"] * n for _ in range(n)]
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if flights[i][j] == "1":
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
                else:
                    plan[i][j] = plan[j][i] = "d"
                    cost += d
    for j in range(1, n):
        r0, rj = find(0), find(j)
        if r0 != rj:
            parent[rj] = r0
            plan[0][j] = plan[j][0] = "a"
            cost += a
    print(cost)
    print("\n".join("".join(row) for row in plan))


main()
