from math import gcd

# a raise must be a whole number of percent of this base
PERCENT = 100


def main():
    n, s = map(int, input().split())
    if s > n:
        print(0)
        return
    # jobs[a] is the longest run of jobs from salary s ending at salary a; a
    # raise from a is a whole percent exactly when it is a multiple of
    # a / gcd(a, 100)
    jobs = [0] * (n + 1)
    jobs[s] = 1
    best = 1
    for a in range(s, n + 1):
        here = jobs[a]
        if not here:
            continue
        best = max(best, here)
        step = a // gcd(a, PERCENT)
        for b in range(a + step, n + 1, step):
            if jobs[b] <= here:
                jobs[b] = here + 1
    print(best)


main()
