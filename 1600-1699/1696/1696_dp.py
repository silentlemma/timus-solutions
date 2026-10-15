import sys


def main():
    n, k, p = (int(w) for w in sys.stdin.read().split())
    # salaries by rank must avoid a strictly decreasing triple; the state is
    # a, the largest salary so far, and b, the largest salary that follows a
    # larger one (0 if none); ways[a][b] counts such prefixes modulo p
    ways = [[0] * (k + 1) for _ in range(k + 1)]
    for z in range(1, k + 1):
        ways[z][0] = 1
    for _ in range(n - 1):
        new = [[0] * (k + 1) for _ in range(k + 1)]
        # a new salary z is allowed when z >= b, and turns (a, b) into (a, z) if
        # z < a, or into (z, b) if z >= a
        # z < a: (a, b) -> (a, z) for every b <= z, a prefix sum along the row
        for a in range(1, k + 1):
            row, target = ways[a], new[a]
            running = 0
            for c in range(a):
                running += row[c]
                if c:
                    target[c] = running % p
        # z >= a: (a, b) -> (z, b) for every a <= z, a prefix sum down the column
        for b in range(k):
            running = 0
            for z in range(b + 1, k + 1):
                running += ways[z][b]
                new[z][b] = (new[z][b] + running) % p
        ways = new
    total = sum(sum(row) for row in ways) % p
    # month total + 1 counted from the first month, numbered 1..p in its year
    print(total + 1)


main()
