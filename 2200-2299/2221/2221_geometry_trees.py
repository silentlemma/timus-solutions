import sys


def chain_sizes(x, y, left, right, order, size, turn):
    n = len(x)
    head = [n] * (n + 1)
    tail = [n] * (n + 1)
    count = [0] * (n + 1)
    previous = [n] * n
    following = [n] * n
    for v in reversed(order):
        a, b = left[v], right[v]
        forward = size[a] >= size[b]
        if forward:
            base, small = a, b
            back, ahead = previous, following
            start, end = head[base], tail[base]
            other = head[small]
            sign = turn
        else:
            base, small = b, a
            back, ahead = following, previous
            start, end = tail[base], head[base]
            other = tail[small]
            sign = -turn
        length = count[base]
        c = v
        # Reuse the larger subtree's chain and insert from its nearer end.
        while c != n:
            next_point = other if c == v else ahead[c]
            while length >= 2:
                a = back[end]
                cross = (x[end] - x[a]) * (y[c] - y[a])
                cross -= (y[end] - y[a]) * (x[c] - x[a])
                if cross * sign > 0:
                    break
                end = a
                length -= 1
            if length:
                ahead[end] = c
            else:
                start = c
            back[c] = end
            ahead[c] = n
            end = c
            length += 1
            c = next_point
        if forward:
            head[v], tail[v] = start, end
        else:
            head[v], tail[v] = end, start
        count[v] = length
    return count


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    points = sorted((data[2 * i + 1], data[2 * i + 2], i) for i in range(n))
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    left = [n] * n
    right = [n] * n
    stack = []
    for v in range(n):
        last = n
        while stack and y[stack[-1]] < y[v]:
            last = stack.pop()
        left[v] = last
        if stack:
            right[stack[-1]] = v
        stack.append(v)
    order = []
    stack = [stack[0]]
    while stack:
        v = stack.pop()
        order.append(v)
        if left[v] != n:
            stack.append(left[v])
        if right[v] != n:
            stack.append(right[v])
    size = [0] * (n + 1)
    for v in reversed(order):
        size[v] = size[left[v]] + size[right[v]] + 1
    lower = chain_sizes(x, y, left, right, order, size, 1)
    upper = chain_sizes(x, y, left, right, order, size, -1)
    answer = [0] * n
    for v in range(n):
        answer[points[v][2]] = max(1, lower[v] + upper[v] - 2)
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
