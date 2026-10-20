import sys


def main():
    data = sys.stdin.read().split()
    n, k, s = int(data[0]), int(data[1]), data[2]
    # On a circle every period can be replaced by its gcd with n, so only the
    # divisors of n are tried, from the smallest.
    for d in range(1, n + 1):
        if n % d:
            continue
        best = []
        kept = 0
        for r in range(d):
            part = s[r::d]
            top = max(set(part), key=part.count)
            best.append(top)
            kept += part.count(top)
        if n - kept <= k:
            print(d)
            print("".join(best) * (n // d))
            return


main()
