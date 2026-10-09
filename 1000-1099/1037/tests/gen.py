"""Random requests: a seed, the number of requests, the largest step of the
time between requests, the percentage of allocations and optionally 1 to
start with all blocks taken at time 0. Allocations are never made when all
blocks are taken."""

import heapq
import random
import sys
from collections import deque

BLOCKS = 30000
LIFETIME = 600
MAX_TIME = 65000


def main():
    seed, count, max_step, alloc_pct = (int(x) for x in sys.argv[1:5])
    fill = len(sys.argv) > 5 and sys.argv[5] == "1"
    rng = random.Random(seed)
    last = {}
    expiries = deque()
    freed = []
    fresh = 1
    used = 0
    t = 0
    out = []
    for k in range(count):
        filling = fill and k < BLOCKS
        if not filling:
            t = min(MAX_TIME, t + rng.randint(0, max_step))
        while expiries and expiries[0][0] <= t:
            e, b = expiries.popleft()
            if last[b] + LIFETIME == e:
                used -= 1
                heapq.heappush(freed, b)
        if filling or (rng.randrange(100) < alloc_pct and used < BLOCKS):
            if freed:
                b = heapq.heappop(freed)
            else:
                b, fresh = fresh, fresh + 1
            last[b] = t
            expiries.append((t + LIFETIME, b))
            used += 1
            out.append("%d +" % t)
        else:
            b = (
                rng.randint(1, min(fresh + 1, BLOCKS))
                if rng.randrange(10)
                else rng.randint(1, BLOCKS)
            )
            if b in last and last[b] + LIFETIME > t:
                last[b] = t
                expiries.append((t + LIFETIME, b))
            out.append("%d . %d" % (t, b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
