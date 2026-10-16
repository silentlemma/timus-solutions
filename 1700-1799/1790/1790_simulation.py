import sys


def spread(run, n):
    lo, hi = run
    if lo > hi:
        return run
    return (lo - 1 if lo > 1 else lo + 1, hi + 1 if hi < n else hi - 1)


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    # runs[p] = (lo, hi): the pedestals lo, lo + 2, ..., hi of parity p
    # where the artifact may be; empty when lo > hi
    runs = [(2, n - n % 2), (1, n - 1 + n % 2)]
    for x in map(int, data[2:2 + m]):
        lo, hi = runs[x % 2]
        # a touch inside the run leaves a hole that the next move fills
        # again, so only a touch at an end shrinks it
        if x == lo:
            runs[x % 2] = (lo + 2, hi)
        elif x == hi:
            runs[x % 2] = (lo, hi - 2)
        # every step flips the parity of the pedestal
        runs = [spread(runs[1], n), spread(runs[0], n)]
    print("YES" if all(lo > hi for lo, hi in runs) else "NO")


main()
