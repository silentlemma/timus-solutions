"""Checker: the output gives every boy a different girl, and in every
pair with a child who likes someone the boy likes his partner or the
girl likes hers."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    k = int(data[0])
    boy_likes = [int(x) for x in data[1 : 1 + k]]
    girl_likes = [int(x) for x in data[1 + k : 1 + 2 * k]]
    got = open(output).read().split()
    if len(got) != k or not all(x.isdigit() for x in got):
        fail("expected %d girl numbers" % k)
    pairs = [int(x) for x in got]
    if sorted(pairs) != list(range(1, k + 1)):
        fail("every girl must be in exactly one pair")
    for boy, girl in enumerate(pairs, 1):
        in_love = boy_likes[boy - 1] != 0 or girl_likes[girl - 1] != 0
        if in_love and boy_likes[boy - 1] != girl and girl_likes[girl - 1] != boy:
            fail("boy %d and girl %d like neither each other" % (boy, girl))


if __name__ == "__main__":
    main()
