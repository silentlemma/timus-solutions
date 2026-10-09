import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, pos = data[0], 1
    children = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        while data[pos] != 0:
            children[v].append(data[pos])
            pos += 1
        pos += 1
    # an iterative depth-first search: a member is appended after all its
    # descendants, so the reversed list puts everyone before their descendants
    done, order = [False] * (n + 1), []
    for root in range(1, n + 1):
        if done[root]:
            continue
        done[root] = True
        stack = [(root, iter(children[root]))]
        while stack:
            v, it = stack[-1]
            c = next(it, None)
            if c is None:
                stack.pop()
                order.append(v)
            elif not done[c]:
                done[c] = True
                stack.append((c, iter(children[c])))
    print(*reversed(order))


main()
