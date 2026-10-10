import sys

WHOLE = 10000


def main():
    data = iter(sys.stdin.read().split())
    n = int(next(data))
    given = []
    for _ in range(n):
        next(data)
        given.append(int(next(data)) if next(data) == "1" else None)
    # shares never grow down the list, so an unknown share is at least the
    # next given one (or 1) and at most the last given one before it (or
    # 100%); every total between the two extremes can be reached
    low, high = [0] * n, [0] * n
    floor = 1
    for i in range(n - 1, -1, -1):
        floor = given[i] if given[i] is not None else floor
        low[i] = floor
    ceiling = WHOLE
    for i in range(n):
        ceiling = given[i] if given[i] is not None else ceiling
        high[i] = ceiling
    print("YES" if sum(low) <= WHOLE <= sum(high) else "NO")


main()
