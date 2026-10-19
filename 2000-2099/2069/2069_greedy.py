import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    v = data[2:2 + n]
    h = data[2 + n:2 + n + m]
    # one turn: down the left street and along the bottom, or along the top and down the right
    best = max(min(v[0], h[-1]), min(h[0], v[-1]))
    # two turns: the middle street is the best one of its kind
    best = max(best, min(h[0], max(v), h[-1]), min(v[0], max(h), v[-1]))
    print(best)


main()
