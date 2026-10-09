import heapq
import sys

FACES = 6


def canonical(comp):
    """Relabel the blocks of a partition in order of first appearance."""
    names = {}
    return tuple(names.setdefault(c, len(names)) for c in comp)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    # a state: the partition of the faces into connected groups, the faces
    # that have dominoes and the faces of odd degree
    comp = list(range(FACES))
    active = 0
    odd = 0
    for k in range(n):
        a, b = data[1 + 2 * k] - 1, data[2 + 2 * k] - 1
        active |= 1 << a | 1 << b
        odd ^= 1 << a ^ 1 << b
        ca, cb = comp[a], comp[b]
        comp = [ca if c == cb else c for c in comp]
    start = (canonical(comp), active, odd)

    def done(state):
        comp, active, odd = state
        groups = {comp[v] for v in range(FACES) if active >> v & 1}
        return len(groups) == 1 and bin(odd).count("1") <= 2

    # Dijkstra over the states: adding the domino (a, b) costs a + b, joins
    # the groups of a and b and flips the parity of both faces
    dist = {start: 0}
    parent = {start: None}
    heap = [(0, start)]
    while heap:
        d, state = heapq.heappop(heap)
        if d > dist[state]:
            continue
        if done(state):
            break
        comp, active, odd = state
        for a in range(FACES):
            for b in range(a + 1, FACES):
                ca, cb = comp[a], comp[b]
                merged = canonical([ca if c == cb else c for c in comp])
                nxt = (merged, active | 1 << a | 1 << b, odd ^ 1 << a ^ 1 << b)
                cost = d + a + b + 2
                if cost < dist.get(nxt, cost + 1):
                    dist[nxt] = cost
                    parent[nxt] = (state, a + 1, b + 1)
                    heapq.heappush(heap, (cost, nxt))
    added = []
    while parent[state] is not None:
        state, a, b = parent[state]
        added.append((a, b))
    out = [str(d), str(len(added))] + ["%d %d" % e for e in added]
    print("\n".join(out))


main()
