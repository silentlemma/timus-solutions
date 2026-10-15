import sys

WRAP = 4  # a fifth bacterium leaves one: counts go 1, 2, 3, 4, 1, ...
DEPTH = 10000  # each branch nests a call, at most one per cell


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    total = n * m
    # need[v]: how many still-free neighbours v must see settled after it,
    # modulo 4, stored as 1..4 like the picture; deg[v]: free neighbours
    need = [int(w) for w in data[2 : 2 + total]]
    adj = [[] for _ in range(total)]
    for r in range(n):
        for c in range(m):
            v = r * m + c
            if r:
                adj[v].append(v - m)
            if r + 1 < n:
                adj[v].append(v + m)
            if c:
                adj[v].append(v - 1)
            if c + 1 < m:
                adj[v].append(v + 1)
    deg = [len(a) for a in adj]
    alive = [True] * total

    def kind(v):
        """'src' if v must come before all free neighbours, 'snk' if after
        all, '?' if either (an inner cell showing 1), None if neither yet,
        'bad' if no order can give its count"""
        d, k = deg[v], need[v]
        if k != 1 and k - 1 > d:
            return "bad"
        if d < WRAP and k == d + 1:
            return "src"
        if d < WRAP and k == 1:
            return "snk"
        if d == WRAP and k == 1:
            return "?"
        return None

    def take(v, first):
        """settle v before (first) or after all its free neighbours"""
        alive[v] = False
        for u in adj[v]:
            if alive[u]:
                deg[u] -= 1
                if not first:  # u now sees v settle after it
                    need[u] = need[u] - 1 or WRAP

    def components(cells):
        inside = set(cells)
        seen = set()
        parts = []
        for s in cells:
            if s in seen:
                continue
            seen.add(s)
            part = [s]
            for v in part:
                for u in adj[v]:
                    if u in inside and alive[u] and u not in seen:
                        seen.add(u)
                        part.append(u)
            parts.append(part)
        return parts

    def counts_fit(cells):
        """necessary: the later-neighbour counts must add up to the edges,
        and touching undecided cells must split into firsts and lasts"""
        edges = sum(deg[v] for v in cells) // 2
        fixed = sum(need[v] - 1 for v in cells if need[v] != 1 or deg[v] < WRAP)
        open_cells = [v for v in cells if kind(v) == "?"]
        if (edges - fixed) % WRAP or not 0 <= (edges - fixed) // WRAP <= len(open_cells):
            return False
        firsts = (edges - fixed) // WRAP
        reach = 1  # bit s: s firsts are possible among the groups so far
        undecided = set(open_cells)
        seen = set()
        for s in open_cells:
            if s in seen:
                continue
            seen.add(s)
            group, colour = [s], [0, 0]
            for v in group:
                colour[(v // m + v % m) % 2] += 1
                for u in adj[v]:
                    if alive[u] and u in undecided and u not in seen:
                        seen.add(u)
                        group.append(u)
            reach = (reach << colour[0]) | (reach << colour[1])
        return bool(reach >> firsts & 1)

    def solve(cells):
        """an order of the free cells, or None"""
        head, tail = [], []
        cells = list(cells)
        while True:
            queue = [v for v in cells if kind(v) in ("src", "snk", "bad")]
            moved = False
            while queue:
                v = queue.pop()
                if not alive[v]:
                    continue
                k = kind(v)
                if k == "bad":
                    return None
                if k not in ("src", "snk"):
                    continue
                take(v, k == "src")
                (head if k == "src" else tail).append(v)
                moved = True
                queue.extend(u for u in adj[v] if alive[u])
            cells = [v for v in cells if alive[v]]
            if not moved or not cells:
                break
        if not cells:
            return head + tail[::-1]
        parts = components(cells)
        if len(parts) > 1:
            middle = []
            for part in parts:
                order = solve(part)
                if order is None:
                    return None
                middle += order
            return head + middle + tail[::-1]
        # the first cell of any order comes before all its neighbours, so
        # with no forced cell left it must be an undecided one
        open_cells = [v for v in cells if kind(v) == "?"]
        if not open_cells or not counts_fit(cells):
            return None
        # an undecided cell comes before or after all its neighbours in any
        # order, so trying both ways for one of them misses nothing
        pick = open_cells[0]
        rest = [v for v in cells if v != pick]
        for first in (True, False):
            saved = (need[:], deg[:], alive[:])
            take(pick, first)
            order = solve(rest)
            need[:], deg[:], alive[:] = saved
            if order is not None:
                middle = [pick] + order if first else order + [pick]
                return head + middle + tail[::-1]
        return None

    sys.setrecursionlimit(DEPTH)
    order = solve(range(total))
    if order is None:
        print("No")
    else:
        print("Yes")
        print("\n".join("%d %d" % (v // m + 1, v % m + 1) for v in order))


main()
