from math import gcd


def pairs(k):
    return k * (k - 1) // 2


def main():
    a, b, n = (int(v) for v in input().split())
    big, small = max(a, b), min(a, b)

    def shared(m):
        """Pairs among the first m sleepers on one page of both notebooks:
        walk the pages of the larger size, each cut by the smaller pages
        into a head, whole pages and a tail."""
        total = 0
        for start in range(0, m, big):
            end = min(start + big, m)
            cut = (start // small + 1) * small
            if cut >= end:
                total += pairs(end - start)
            else:
                whole, tail = divmod(end - cut, small)
                total += pairs(cut - start) + whole * pairs(small) + pairs(tail)
        return total

    # both page breaks repeat every lcm(a, b) sleepers, and so do the pairs
    period = a // gcd(a, b) * b
    if period <= n:
        both = n // period * shared(period) + shared(n % period)
    else:
        both = shared(n)
    vasily = n // a * pairs(a) + pairs(n % a)
    print(vasily - both)


main()
