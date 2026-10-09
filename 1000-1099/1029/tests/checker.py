"""Checker: the rooms form a walk that starts on the first floor, goes one
floor up through the same room or to a neighbouring room on the same floor,
ends on the top floor, and costs exactly the minimum."""

import sys


def cost(fee, rooms):
    """The cost of the walk, or a reason why it is not a walk."""
    m, n = len(fee), len(fee[0])
    if not rooms or any(not 1 <= r <= n for r in rooms):
        return None, "rooms must be between 1 and %d" % n
    floor, total = 0, fee[0][rooms[0] - 1]
    for prev, room in zip(rooms, rooms[1:]):
        if room == prev:
            floor += 1
            if floor >= m:
                return None, "the walk goes above the top floor"
        elif abs(room - prev) != 1:
            return None, "room %d does not follow room %d" % (room, prev)
        total += fee[floor][room - 1]
    if floor != m - 1:
        return None, "the walk ends on floor %d of %d" % (floor + 1, m)
    return total, None


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    m, n = data[0], data[1]
    fee = [data[2 + i * n : 2 + (i + 1) * n] for i in range(m)]
    best, _ = cost(fee, [int(x) for x in open(expected).read().split()])
    try:
        rooms = [int(x) for x in open(output).read().split()]
    except ValueError:
        print("non-integer token")
        sys.exit(1)
    total, reason = cost(fee, rooms)
    if reason:
        print(reason)
        sys.exit(1)
    if total != best:
        print("the walk costs %d, the minimum is %d" % (total, best))
        sys.exit(1)


main()
