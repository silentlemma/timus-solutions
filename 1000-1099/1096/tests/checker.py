"""Checker: IMPOSSIBLE only when no exchange sequence exists; otherwise the
count must be the fewest exchanges, found here by layers of reachable
plates, and replaying the listed exchanges (a driver swaps when the new
driver's plate shows the route of his bus) must end with a plate showing T."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = list(map(int, open(inp).read().split()))
    k = tok[0]
    route = [tok[1 + 2 * i] for i in range(k)]
    back = [tok[2 + 2 * i] for i in range(k)]
    t, s1, s2 = tok[1 + 2 * k : 4 + 2 * k]
    # layer by layer: plates reachable after exactly d exchanges
    seen = set()
    layer = [(s1, s2)]
    best = None
    for d in range(1, k + 1):
        nxt = []
        for plate in layer:
            for j in range(k):
                if j not in seen and route[j] in plate:
                    seen.add(j)
                    nxt.append((route[j], back[j]))
        if any(t in plate for plate in nxt):
            best = d
            break
        if not nxt:
            break
        layer = nxt
    got = open(output).read().split()
    if best is None:
        if got != ["IMPOSSIBLE"]:
            fail("expected IMPOSSIBLE")
        return
    try:
        nums = [int(x) for x in got]
    except ValueError:
        fail("expected numbers")
    if not nums or nums[0] != best or len(nums) != best + 1:
        fail("expected %d exchanges" % best)
    plates = [(route[i], back[i]) for i in range(k)]
    mine = (s1, s2)
    for j in nums[1:]:
        if not 1 <= j <= k or route[j - 1] not in mine:
            fail("the driver of bus %d does not agree to exchange" % j)
        mine, plates[j - 1] = plates[j - 1], mine
    if t not in mine:
        fail("the final plate does not show route %d" % t)


main()
