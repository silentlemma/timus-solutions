"""Check the number of problems against the stored one and the plan: no
sponsor twice in a problem, at most K sponsors per problem, and every
sponsor in exactly s_i problems."""

import sys

ARGS = 4


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, k = data[0], data[1]
    wanted = data[2:2 + n]
    best = int(open(expected).read().split()[0])
    words = open(output).read().split()
    try:
        got = list(map(int, words))
    except ValueError:
        raise Bad("expected integers")
    if not got or got[0] != best:
        raise Bad("expected %d problems" % best)
    pos = 1
    seen = [0] * (n + 1)
    for _ in range(best):
        if pos >= len(got):
            raise Bad("too few problem lines")
        size = got[pos]
        sponsors = got[pos + 1:pos + 1 + size]
        pos += 1 + size
        if size < 0 or size > k or len(sponsors) != size:
            raise Bad("a problem has a wrong number of sponsors")
        if len(set(sponsors)) != size or not all(1 <= x <= n for x in sponsors):
            raise Bad("repeated or unknown sponsor")
        for x in sponsors:
            seen[x] += 1
    if pos != len(got):
        raise Bad("extra output")
    if seen[1:] != wanted:
        raise Bad("a sponsor appears a wrong number of times")


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
