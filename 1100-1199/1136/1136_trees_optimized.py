import sys


def main():
    post = list(map(int, sys.stdin.buffer.read().split()))
    n = post[0]
    # nodes are input positions, and zero means a missing child
    post[0] = 0
    left, right = [0] * (n + 1), [0] * (n + 1)
    stack = []
    # read backwards, the odd-session order gives every chairman, then the
    # right wing, then the left wing; a stack of the open chairmen rebuilds the
    # tree from that
    for k in range(n, 0, -1):
        if stack and post[k] > post[stack[-1]]:
            right[stack[-1]] = k
        elif stack:
            parent = stack.pop()
            while stack and post[stack[-1]] > post[k]:
                parent = stack.pop()
            left[parent] = k
        stack.append(k)
    # the even-session order is the plain order root, left, right reversed
    order = []
    stack.clear()
    if n:
        stack.append(n)
    while stack:
        node = stack.pop()
        order.append(post[node])
        if right[node]:
            stack.append(right[node])
        if left[node]:
            stack.append(left[node])
    sys.stdout.write("\n".join(map(str, reversed(order))) + "\n")


main()
