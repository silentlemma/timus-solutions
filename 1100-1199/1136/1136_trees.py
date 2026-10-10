import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    post = [int(x) for x in data[1 : 1 + n]]
    # read backwards, the odd-session order gives every chairman, then the
    # right wing, then the left wing; a stack of the open chairmen rebuilds the
    # tree from that
    left, right = {}, {}
    stack = []
    for v in reversed(post):
        if stack and v > stack[-1]:
            right[stack[-1]] = v
        elif stack:
            parent = stack.pop()
            while stack and stack[-1] > v:
                parent = stack.pop()
            left[parent] = v
        stack.append(v)
    # the even-session order is the plain order root, left, right reversed
    order = []
    stack = [post[-1]] if n else []
    while stack:
        v = stack.pop()
        order.append(v)
        for child in (right.get(v), left.get(v)):
            if child is not None:
                stack.append(child)
    sys.stdout.write("\n".join(map(str, reversed(order))) + "\n")


main()
