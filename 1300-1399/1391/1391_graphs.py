import sys

LONGEST = 16  # the longest cycle counted: no snake of length 18 gets out
SHORTEST = 4  # the shortest cycle on a grid
LENGTHS = range(2, 18)  # the snake lengths to answer for


def main():
    h, w, r0, c0, *rows = sys.stdin.read().split()
    h, w = int(h), int(w)
    start = (int(r0) - 1) * w + int(c0) - 1
    free = [rows[r][c] == "." for r in range(h) for c in range(w)]
    free[start] = True
    near = [[] for _ in range(h * w)]
    for v in range(h * w):
        r, c = divmod(v, w)
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < h and 0 <= nc < w and free[nr * w + nc]:
                near[v].append(nr * w + nc)
    # distances from the entrance
    dist = [-1] * (h * w)
    dist[start] = 0
    order = [start]
    for v in order:
        for u in near[v]:
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                order.append(u)
    # rank: breadth-first position; a cycle is found from its first cell in this order
    rank = [len(order)] * (h * w)
    for i, v in enumerate(order):
        rank[v] = i
    best = {}
    needed = set(range(SHORTEST, LONGEST + 1, 2))
    for root in order:
        if not needed:
            break
        rr, rc = divmod(root, w)
        limit = max(needed)
        on_path = {root}

        def walk(v, steps):
            for u in near[v]:
                if u == root and steps + 1 >= SHORTEST and steps + 1 in needed:
                    best[steps + 1] = dist[root]
                    needed.discard(steps + 1)
                elif u not in on_path and rank[u] > rank[root]:
                    ur, uc = divmod(u, w)
                    if steps + 1 + abs(ur - rr) + abs(uc - rc) <= limit:
                        on_path.add(u)
                        walk(u, steps + 1)
                        on_path.discard(u)

        walk(root, 0)
    out = []
    for length in LENGTHS:
        times = [2 * best[c] + c for c in best if c >= length]
        out.append(str(min(times)) if times else "-1")
    print("\n".join(out))


main()
