import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    flags = sorted(
        ((int(data[2 * i + 2]), int(data[2 * i + 1]), i + 1) for i in range(n)), reverse=True
    )
    # down the slope the x coordinates must zigzag; the longest zigzag keeps
    # the first flag, the last one of every run in one direction, and the end
    xs = [x for _, x, _ in flags]
    path = [flags[0][2]]
    for i in range(1, n):
        last = i == n - 1
        turns = not last and (xs[i] - xs[i - 1] > 0) != (xs[i + 1] - xs[i] > 0)
        if last or turns:
            path.append(flags[i][2])
    print(len(path))
    print(" ".join(map(str, path)))


main()
