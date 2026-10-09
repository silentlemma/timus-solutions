import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rating = [0] + [int(x) for x in data[1 : n + 1]]
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    i = n + 1
    while i + 1 < len(data):
        child, boss = int(data[i]), int(data[i + 1])
        if child == 0:
            break
        parent[child] = boss
        children[boss].append(child)
        i += 2
    # a breadth-first order from the roots puts every boss before the subordinates
    order = [v for v in range(1, n + 1) if parent[v] == 0]
    for v in order:
        order.extend(children[v])
    # take[v], skip[v]: the best sum in the subtree of v with v invited or not
    take = [0] * (n + 1)
    skip = [0] * (n + 1)
    total = 0
    for v in reversed(order):
        take[v] += rating[v]
        best = max(take[v], skip[v])
        p = parent[v]
        if p == 0:
            total += best
        else:
            take[p] += skip[v]
            skip[p] += best
    print(total)


main()
