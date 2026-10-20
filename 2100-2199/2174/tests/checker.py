"""Check the verdict against the stored one and, for YES, that the printed
pairs use exactly the given notes and every pair sums to a prime."""

import sys

ARGS = 4


class Bad(Exception):
    pass


def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n = data[0]
    notes = sorted(data[1:n + 1])
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] not in ("YES", "NO"):
        raise Bad("expected YES or NO")
    if got[0] != want:
        raise Bad("wrong verdict %s" % got[0])
    if want == "NO":
        if len(got) != 1:
            raise Bad("extra output after NO")
        return
    try:
        values = list(map(int, got[1:]))
    except ValueError:
        raise Bad("expected integers")
    if len(values) != n:
        raise Bad("expected %d numbers in pairs" % n)
    if sorted(values) != notes:
        raise Bad("the pairs do not use exactly the given notes")
    for a, b in zip(values[0::2], values[1::2]):
        if not is_prime(a + b):
            raise Bad("%d + %d is not prime" % (a, b))


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
