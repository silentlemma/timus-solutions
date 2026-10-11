import sys

FIXED = 153  # 1 + 125 + 27: every multiple of 3 ends here
TEN = 10


def cubes(x):
    s = 0
    while x:
        x, d = divmod(x, TEN)
        s += d * d * d
    return s


def main():
    words = iter(sys.stdin.buffer.read().split())

    def number():
        return int(next(words))

    out = []
    for _ in range(number()):
        n, k, dist = number(), number(), number()
        # the gap before base N is F applied N - 1 times to K; from a
        # multiple of 3 it reaches 153 within 14 steps and stays there
        gap = k
        for _ in range(n - 1):
            if gap == FIXED:
                break
            gap = cubes(gap)
        out.append(gap - dist)
    sys.stdout.write("".join("%d\n" % x for x in out))


main()
