DIGITS = 10


def main():
    n, s = map(int, input().split())
    half = s // 2
    if s % 2 or half > (DIGITS - 1) * n:
        print(0)
        return
    # ways[t]: the number of strings of the digits seen so far with digit sum t
    ways = [1] + [0] * half
    for _ in range(n):
        ways = [sum(ways[t - d] for d in range(min(DIGITS - 1, t) + 1)) for t in range(half + 1)]
    # the two halves are chosen independently
    print(ways[half] ** 2)


main()
