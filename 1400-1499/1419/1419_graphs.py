import sys

DEGREE = 3
# the symbol each kind of gap may hold, and the step it makes between islands
SLOTS = {(0, 1): {"-": (0, 1)}, (1, 0): {"|": (1, 0)}, (1, 1): {"\\": (1, 1), "/": (1, -1)}}


def real_map(w, h, lines):
    adj = [[] for _ in range(w * h)]
    edges = 0
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if r % 2 == 0 and c % 2 == 0 or ch == " ":
                continue
            step = SLOTS[r % 2, c % 2].get(ch)
            if step is None:
                return False  # a symbol that joins nothing in this gap
            dr, dc = step
            a = (r - dr) // 2 * w + (c - dc) // 2
            b = a + dr * w + dc
            adj[a].append((b, edges))
            adj[b].append((a, edges))
            edges += 1
    if any(len(v) != DEGREE for v in adj):
        return False
    # iterative low-link search: a tree edge to v is a bridge if low[v] > tin[parent]
    tin = [-1] * (w * h)
    low = [0] * (w * h)
    tin[0] = 0
    timer = 0
    stack = [(0, -1, 0)]
    while stack:
        v, via, k = stack[-1]
        if k < len(adj[v]):
            stack[-1] = (v, via, k + 1)
            u, e = adj[v][k]
            if e == via:
                continue
            if tin[u] < 0:
                timer += 1
                tin[u] = low[u] = timer
                stack.append((u, e, 0))
            else:
                low[v] = min(low[v], tin[u])
            continue
        stack.pop()
        if stack:
            p = stack[-1][0]
            low[p] = min(low[p], low[v])
            if low[v] > tin[p]:
                return False
    return min(tin) >= 0


def main():
    lines = sys.stdin.read().split("\n")
    m, n = map(int, lines[0].split())
    picture = [line.rstrip("\r").ljust(m)[:m] for line in lines[1 : 1 + n]]
    picture += [" " * m] * (n - len(picture))
    ok = real_map((m + 1) // 2, (n + 1) // 2, picture)
    print("Island world" if ok else "Just a picture")


main()
