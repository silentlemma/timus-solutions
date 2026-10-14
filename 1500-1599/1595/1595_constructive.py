import sys

CHUNK = 4096  # terms written at a time, to keep the memory small


def main():
    n = int(sys.stdin.read())
    out = []
    used = set()
    total = 0  # the sum of the terms so far
    for m in range(1, n + 1):
        # put a large x at position k and then m at k + 1: x must make the
        # sum divisible by k, and x + m divisible by k + 1
        k = 2 * m - 1
        a = -total % k
        b = (-total - m) % (k + 1)
        # x = a + k t, and k = -1 modulo k + 1, so t = a - b modulo k + 1
        step = k * (k + 1)
        x = a + k * ((a - b) % (k + 1))
        if x <= n:
            x += (n - x) // step * step + step
        while x in used:
            x += step
        used.add(x)
        out.append("%d %d" % (x, m))
        total += x + m
        if len(out) == CHUNK:
            sys.stdout.write(" ".join(out) + " ")
            out = []
    sys.stdout.write(" ".join(out) + "\n")


main()
