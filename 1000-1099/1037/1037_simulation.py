import sys
from collections import deque
from heapq import heappop, heappush

BLOCKS = 30000
LIFETIME = 600


def main():
    data = sys.stdin.buffer.read().split()
    # expiry[b]: when block b becomes free, unless it is accessed again
    expiry = [0] * (BLOCKS + 1)
    busy = [False] * (BLOCKS + 1)
    # times never decrease, so the expiries are queued in order; an entry is
    # stale when the block was accessed again later
    expiries = deque()
    freed = []
    fresh = 1
    out = []
    i = 0
    while i < len(data):
        t = int(data[i])
        op = data[i + 1]
        i += 2
        while expiries and expiries[0][0] <= t:
            e, b = expiries.popleft()
            if busy[b] and expiry[b] == e:
                busy[b] = False
                heappush(freed, b)
        if op == b"+":
            # freed blocks are all smaller than the never used ones
            if freed:
                b = heappop(freed)
            else:
                b, fresh = fresh, fresh + 1
            out.append(str(b))
        else:
            b = int(data[i])
            i += 1
            if not busy[b]:
                out.append("-")
                continue
            out.append("+")
        busy[b] = True
        expiry[b] = t + LIFETIME
        expiries.append((expiry[b], b))
    sys.stdout.write("\n".join(out) + "\n")


main()
