import sys


def digits(v, base):
    out = []
    while v:
        out.append(v % base)
        v //= base
    return out[::-1]


def fits(x, y, base):
    it = iter(digits(x, base))
    return all(d in it for d in digits(y, base))


def answer(x, y):
    base = 2
    while base * base <= x:
        if fits(x, y, base):
            return base
        base += 1
    # from here on x has two digits x // b and x % b, and y must be one of them
    best = None
    low = max(base, x // (y + 1) + 1)
    if low <= x // y:
        best = low
    # x % b == y means that b divides x - y and is larger than y
    least = max(base, y + 1)
    n = x - y
    d = 1
    while d * d <= n:
        if n % d == 0:
            for b in (d, n // d):
                if b >= least and (best is None or b < best):
                    best = b
        d += 1
    return best


def main():
    x, y = map(int, sys.stdin.read().split())
    best = answer(x, y)
    print("No solution" if best is None else best)


main()
