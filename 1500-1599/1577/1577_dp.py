import sys

MOD = 10**9 + 7


def main():
    a, b = sys.stdin.read().split()[:2]
    n, m = len(a), len(b)
    # length[j] and count[j]: the shortest common supersequences of a[i:] and
    # b[j:], their length and number; row i needs only row i + 1
    length = list(range(m, -1, -1))  # i = n: only b[j:] itself
    count = [1] * (m + 1)
    for i in range(n - 1, -1, -1):
        below_len, below_cnt = length, count
        length = [0] * (m + 1)
        count = [0] * (m + 1)
        length[m], count[m] = n - i, 1  # only a[i:] itself
        ai = a[i]
        for j in range(m - 1, -1, -1):
            if ai == b[j]:
                # the first letter is the common one and covers both
                length[j] = below_len[j + 1] + 1
                count[j] = below_cnt[j + 1]
            else:
                # the first letter is a[i] or b[j]; the two kinds of strings
                # differ in their first letter, so their numbers add up
                take_a, take_b = below_len[j], length[j + 1]
                best = min(take_a, take_b)
                length[j] = best + 1
                ways = 0
                if take_a == best:
                    ways += below_cnt[j]
                if take_b == best:
                    ways += count[j + 1]
                count[j] = ways % MOD
    print(count[0])


main()
