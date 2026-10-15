"""Checker: as many boxes as the expected answer, all different, each
holding a wanted coin, and no more boxes than the wanted coins they hold
together."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = [int(w) for w in open(source).read().split()]
    k = data[1]
    boxes, pos = [], 2
    for _ in range(k):
        size = data[pos]
        boxes.append(set(data[pos + 1:pos + 1 + size]))
        pos += 1 + size
    wanted = set(data[pos + 1:pos + 1 + data[pos]])
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not words:
        raise Bad("empty output")
    count = int(words[0])
    if count != want:
        raise Bad("%d boxes instead of %d" % (count, want))
    picked = [int(w) for w in words[1:]]
    if len(picked) != count:
        raise Bad("%d box numbers for %d boxes" % (len(picked), count))
    if len(set(picked)) != count or not all(1 <= b <= k for b in picked):
        raise Bad("box numbers repeat or are out of range")
    covered = set()
    for b in picked:
        if not boxes[b - 1] & wanted:
            raise Bad("box %d holds no wanted coin" % b)
        covered |= boxes[b - 1] & wanted
    if count > len(covered):
        raise Bad("%d boxes are worth only %d coins" % (count, len(covered)))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
