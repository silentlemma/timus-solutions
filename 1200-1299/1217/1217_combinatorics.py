DIGITS = 10


def sums(k):
    """ways[s]: strings of k digits with digit sum s"""
    ways = [1]
    for _ in range(k):
        nxt = [0] * (len(ways) + DIGITS - 1)
        for s, w in enumerate(ways):
            for d in range(DIGITS):
                nxt[s + d] += w
        ways = nxt
    return ways


def matching(k, m):
    """pairs of a k-digit and an m-digit string with equal digit sums"""
    a, b = sums(k), sums(m)
    return sum(x * y for x, y in zip(a, b))


def main():
    n = int(input())
    half = n // 2
    # group the positions by half and by parity: lucky both ways means the
    # odd digits of the first half sum like the even ones of the second, and
    # the even digits of the first half like the odd ones of the second
    size = {}
    for p in range(1, n + 1):
        key = (p <= half, p % 2)
        size[key] = size.get(key, 0) + 1
    first = matching(size.get((True, 1), 0), size.get((False, 0), 0))
    second = matching(size.get((True, 0), 0), size.get((False, 1), 0))
    print(first * second)


main()
