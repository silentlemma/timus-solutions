from array import array
from sys import stdin


def main():
    read = stdin.buffer.readline
    n = int(read())
    degree = array("i", [0]) * n
    neighbor = array("i", [0]) * n
    weight = array("i", [0]) * n
    for _ in range(n - 1):
        a, b, cost = map(int, read().split())
        a -= 1
        b -= 1
        degree[a] += 1
        degree[b] += 1
        neighbor[a] ^= b
        neighbor[b] ^= a
        weight[a] ^= cost
        weight[b] ^= cost

    leaves = [v for v in range(n) if degree[v] == 1]
    size = array("i", [1]) * n
    total = 0
    for v in leaves:
        if degree[v] == 0:
            continue
        u, cost = neighbor[v], weight[v]
        total += cost * size[v] * (n - size[v])
        size[u] += size[v]
        degree[v] = 0
        degree[u] -= 1
        neighbor[u] ^= v
        weight[u] ^= cost
        if degree[u] == 1:
            leaves.append(u)
    print(f"{2 * total / (n * (n - 1)):.4f}")


main()
