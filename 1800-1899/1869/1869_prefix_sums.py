import sys

SEATS = 36


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    # change[k] is how many people get on at station k minus how many get
    # off there; the eastbound and westbound trains are counted apart
    east, west = [0] * (n + 1), [0] * (n + 1)
    for i in range(n):
        row = data[1 + i * n:1 + (i + 1) * n]
        for j, a in enumerate(row):
            if i < j:
                east[i] += a
                east[j] -= a
            elif i > j:
                west[j] += a
                west[i] -= a
    best = load_e = load_w = 0
    for k in range(n):
        load_e += east[k]
        load_w += west[k]
        best = max(best, load_e, load_w)
    print(-(-best // SEATS))


main()
