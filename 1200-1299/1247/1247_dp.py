import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    s, n = data[0], data[1]
    # the sum of A_i - 1 over every segment must stay at most N, so only the
    # largest such sum matters: Kadane's scan keeps the best one ending here
    best = here = 0
    for a in data[2 : 2 + s]:
        here = max(here, 0) + a - 1
        if here > best:
            best = here
    print("YES" if best <= n else "NO")


main()
