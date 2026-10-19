import sys

ALICE = 1
FIELDS = 3  # kid, start, duration


def main():
    length, total, va, vb, n, *rest = map(int, sys.stdin.buffer.read().split())
    # riding in opposite directions, they meet whenever the distance ridden by
    # both together reaches a new multiple of the length; the intervals of one
    # kid do not overlap, so their durations add up
    resting = [0, 0]
    for kid, _, duration in zip(*[iter(rest)] * FIELDS):
        resting[0 if kid == ALICE else 1] += duration
    ridden = va * (total - resting[0]) + vb * (total - resting[1])
    print(ridden // length)


main()
