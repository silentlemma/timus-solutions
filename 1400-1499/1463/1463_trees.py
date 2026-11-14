import sys


def main():
    read = sys.stdin.buffer.readline
    n, flights = map(int, read().split())
    joy = [0] + list(map(int, read().split()))
    degree = [0] * (n + 1)
    neighbor = [0] * (n + 1)
    weight = [0] * (n + 1)
    for _ in range(flights):
        a, b, c = map(int, read().split())
        degree[a] += 1
        degree[b] += 1
        neighbor[a] ^= b
        neighbor[b] ^= a
        weight[a] ^= c
        weight[b] ^= c

    center = max(range(1, n + 1), key=joy.__getitem__)
    best = joy[center]
    left = right = 0
    arm = [0] * (n + 1)
    child = [0] * (n + 1)
    leaves = [v for v in range(1, n + 1) if degree[v] == 1]
    for v in leaves:
        if not degree[v]:
            continue
        parent = neighbor[v]
        edge = weight[v]
        degree[parent] -= 1
        neighbor[parent] ^= v
        weight[parent] ^= edge
        if degree[parent] == 1:
            leaves.append(parent)

        # Combine this arm with the best one already removed at the parent.
        branch = edge + joy[v] + arm[v]
        total = joy[parent] + branch + arm[parent]
        if total > best:
            best = total
            center, left, right = parent, v, child[parent]
        if branch > arm[parent]:
            arm[parent] = branch
            child[parent] = v

    route = []
    while left:
        route.append(left)
        left = child[left]
    route.reverse()
    route.append(center)
    while right:
        route.append(right)
        right = child[right]
    print(best)
    print(len(route))
    print(" ".join(map(str, route)))


if __name__ == "__main__":
    main()
