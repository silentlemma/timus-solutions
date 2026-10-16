import sys
from operator import mul


def multiply(a, b, mod):
    columns = list(zip(*b))
    return [[sum(map(mul, row, col)) % mod for col in columns] for row in a]


def main():
    n, m, d, mod, q = map(int, sys.stdin.readline().split())
    numbers = iter(int(w) for w in sys.stdin.read().split())
    points = [[next(numbers) for _ in range(n)] for _ in range(q)]
    # the number of routes depends only on how many coordinates differ
    # from the target: a move fixes one of them, changes one of them to
    # another wrong value, or spoils one that was right
    size = n + 1
    step = [[0] * size for _ in range(size)]
    for h in range(size):
        if h > 0:
            step[h][h - 1] = h % mod
            step[h][h] = h * (m - 2) % mod
        if h < n:
            step[h][h + 1] = (n - h) * (m - 1) % mod
    power = [[(1 if i == j else 0) % mod for j in range(size)] for i in range(size)]
    while d:
        if d & 1:
            power = multiply(power, step, mod)
        step = multiply(step, step, mod)
        d >>= 1
    out = []
    for a in points:
        out.append(" ".join(str(power[sum(x != y for x, y in zip(a, b))][0]) for b in points))
    print("\n".join(out))


main()
