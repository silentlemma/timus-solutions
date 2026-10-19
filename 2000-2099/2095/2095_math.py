FIRST = 2  # the first step removes every second day


def quiet(n):
    # among the first n days, step k removes every k-th of those still left,
    # which is n // k of a prefix of length n; it stops mattering once n < k
    k = FIRST
    while n >= k:
        n -= n // k
        k += 1
    return n


def main():
    left, right = map(int, input().split())
    print(quiet(right) - quiet(left - 1))


main()
